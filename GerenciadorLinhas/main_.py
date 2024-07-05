import sqlite3 as sql
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from os import _exit

#Depois criar um programa separado para criar o arquivo sql
class Window():
    def __init__(self, button_width, background_color, font_color, title_font, text_font):
        self.button_width = button_width
        self.background_color = background_color
        self.font_color = font_color
        self.title_font = title_font
        self.text_font = text_font


        #Cria a database
        path = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Arquivos SQL", "*.sql")]
        ) 
        if path == "":
            _exit(0)
        else:
            pass

        self.obj = Gerenciador(path)
        self.main()
    
    def initialize_popUp(self, background_color, title_font, text_font):
        self.background_color = background_color
        self.title_font = title_font
        self.text_font = text_font
    
    def main(self):
        self.window = Tk()
        self.window.resizable(False, False)

        frame = Frame(self.window, padx= 5, pady=5, background=self.background_color, name="gerenciador")
        frame.grid(sticky="nswe")

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        img = ImageTk.PhotoImage(Image.open("GerenciadorLinhas\logo.png"))
        panel = Label(frame, image = img)
        panel.grid(row=0, column=0, columnspan=2)

        title = ttk.Label(frame, text= "Gerenciador de linhas", font=self.title_font, foreground=self.font_color, 
                          background=self.background_color, anchor="center", padding=10)
        title.grid(row=0, column=2, columnspan=5, sticky="nsew")

        self.obj.consultarBanco(frame, self.font_color, self.text_font, self.background_color)

        vazio = ttk.Label(frame, text= "", font=self.text_font, foreground=self.font_color, 
                          background=self.background_color, anchor="center", padding=10)
        vazio.grid(row=999, column=0)

        add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:self.addLinha(), width=self.button_width)
        add.grid(row=1000, column=4, columnspan=3, sticky="nsew")

        self.window.lift()#Vai fazer a janela abrir a cima de tudo
        self.window.attributes("-topmost", True)
        self.window.after_idle(self.window.attributes, '-topmost', False)

        self.window.mainloop()

    def addLinha(self):
        janela = Toplevel()
        janela.configure(background=self.background_color, padx=10, pady=10)

        ttk.Label(janela, text="Insira o código da linha", font=self.text_font, foreground=self.font_color, 
                  background=self.background_color, padding=10).grid(row=0, column=0)
        cod = ttk.Entry(janela, font=self.text_font, width=10)
        cod.grid(row=0, column=1)

        ttk.Label(janela, text="Escreva a cor da linha", font=self.text_font, foreground=self.font_color, 
                  background=self.background_color, padding=10).grid(row=1, column=0)
        cor = ttk.Entry(janela, font=self.text_font, width=10)
        cor.grid(row=1, column=1)

        ttk.Label(janela, text="Quantos cones tem?", font=self.text_font, foreground=self.font_color, 
                  background=self.background_color, padding=10).grid(row=2, column=0)
        qntd = ttk.Entry(janela, font=self.text_font, width=10)
        qntd.grid(row=2, column=1) 

        add = ttk.Button(janela, text="Add", takefocus=False, padding=2, width=self.button_width, 
                         command=lambda:(self.atualizar_frame(cod.get(), cor.get(), qntd.get())))
        add.grid(row=4, column=0)
    
    def popUp(self, mesage):
        janela_msg = Toplevel()
        janela_msg.title("Aviso")
        janela_msg.resizable(False, False)
        janela_msg.configure(background=self.background_color)
        Label(janela_msg, text=mesage, font=self.title_font, pady=15, background=self.background_color).pack()
        Button(janela_msg, text="Fechar", font=self.text_font, command=janela_msg.destroy).pack()
    
    def atualizar_frame(self, cod, cor, qntd):#O problema ta aqui
        # Limpa o frame atual
        for i in self.window.winfo_children():
            i.destroy()

        self.obj.adicionarCorNova(cod, cor, qntd)    
            
        frame = Frame(self.window, padx= 5, pady=5, background=self.background_color, name="gerenciador")
        frame.grid(sticky="nswe")

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        
        img = ImageTk.PhotoImage(Image.open("GerenciadorLinhas\logo.png"))
        panel = Label(frame, image = img)
        panel.grid(row=0, column=0, columnspan=2)

        title = ttk.Label(frame, text= "Gerenciador de linhas", font=self.title_font, foreground=self.font_color, 
                          background=self.background_color, anchor="center", padding=10)
        title.grid(row=0, column=2, columnspan=5, sticky="nsew")

        self.obj.consultarBanco(frame, self.font_color, self.text_font, self.background_color)

        vazio = ttk.Label(frame, text= "", font=self.text_font, foreground=self.font_color, 
                          background=self.background_color, anchor="center", padding=10)
        vazio.grid(row=999, column=0)

        add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:self.addLinha(), width=self.button_width)
        add.grid(row=1000, column=4, columnspan=3, sticky="nsew")

        self.window.lift()#Vai fazer a janela abrir a cima de tudo
        self.window.attributes("-topmost", True)
        self.window.after_idle(self.window.attributes, '-topmost', False)

        self.window.mainloop()




class Gerenciador(Window):
    def __init__(self, path):
        self.initialize_popUp("#b4dff0", "Helvetica 15 bold", "consolas 12 bold")

        self.path = path
        
        self.banco = sql.connect(path)
        self.cursor = self.banco.cursor()

        #verifica se a tabela em questão existe
        self.nome_tabela = "linhas"
        consulta = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{self.nome_tabela}'"
        self.cursor.execute(consulta)
        existe = self.cursor.fetchone() is not None

        if existe == False:
            self.cursor.execute("CREATE TABLE linhas (códigoLinha, corLinha, qntd)")
            self.banco.commit()
        else:
            pass

    def consultarBanco(self, window, font_color, text_font, background_color):#Vai ver quantas linhas tem no banco, pra colocar no hud
        try:
            show = self.cursor.execute("SELECT * from linhas")
            a = 1
            for i in show:
                ttk.Label(window, text="  Código: ", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=0, sticky="w")
                ttk.Label(window, text=i[0], font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=1, sticky="w")
                ttk.Label(window, text="  Cor: ", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=2, sticky="w")
                ttk.Label(window, text=i[1], font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=3, sticky="w")
                ttk.Label(window, text="  Quantidade: ", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=4, sticky="w")
                ttk.Label(window, text=i[2], font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=5, sticky="w")
                ttk.Button(window, text="+", width=1, command=lambda:self.addumaLinha(i[0], i[2]), 
                           takefocus=False).grid(row=a, column=6, sticky="e")
                ttk.Button(window, text="-", width=1, command=lambda:self.delumaLinha(i[0], i[2]), 
                           takefocus=False).grid(row=a, column=7, sticky="e")
                ttk.Button(window, text="🗑️", width=2, command=lambda:self.delLinha(i[0]), takefocus=False).grid(row=a, column=8, sticky="e")
                a += 1
                #Vai chamar as funções aqui, com os dados que ja tao negoçados aqui
                if a == 11:
                    ttk.Label(window, text="", font=text_font, foreground=font_color, 
                              background=background_color).grid(row=a, column=0, sticky="w")
                    ttk.Button(window, text="Próximo", command=lambda:self.proxPag(), 
                               takefocus=False).grid(row=a+1, column=6, columnspan=3, sticky="e")
                    break
        except:
            print("Deu errado")

    def addumaLinha(self, cod, qntd):
        pass

    def delumaLinha(self, cod, cor, qntd):
        pass

    def delLinha(self, cod, cor, qntd):
        pass

    def proxPag(self):
        pass
    
    def adicionarCorNova(self, cod, cor, qntd):#Vai jogar uma nova cor de linha no banco de dados
        #Verifica se o cod é um número
        try:
            # Verifica se o código é um número
            int(cod)
            
            # Verifica se a cor está correta e escrita por extenso
            num = range(10)

            if any(char.isdigit() for char in cor):
                raise ValueError
            else:      
                cor = cor.lower().strip()
            
            # Verifica se a quantidade é um número
            qntd = int(qntd)

            consulta = f"SELECT * FROM {self.nome_tabela} WHERE códigoLinha = ?"
            self.cursor.execute(consulta, (cod,))
            resultado = self.cursor.fetchone() 

            if resultado is None:
                self.cursor.execute("INSERT INTO linhas VALUES (?, ?, ?)", (cod, cor, qntd))
                self.banco.commit()
                print("Adicionado no banco")
            else:
                raise Exception("Cor ja existente")

        except ValueError:
            super().popUp(mesage="Insira um número válido em código ou quantidade!\nOu se a cor esta escrita por extenso")
        except AttributeError:
            super().popUp(mesage="Escreva a cor por extenso!")
        except Exception as e:
            if str(e) == "Cor ja existente":
                super().popUp(mesage="Cor já existente no banco de dados")
  

if __name__ == '__main__':
    app = Window(15, "#b4dff0", "#030608", "Helvetica 15 bold", "consolas 12 bold")
    
