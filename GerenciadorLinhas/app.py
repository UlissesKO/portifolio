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
        add.grid(row=1000, column=3, columnspan=3, sticky="nsew")

        delete = ttk.Button(frame, text="Remover linha", takefocus=False, command=lambda:self.delLinha(), width=self.button_width)
        delete.grid(row=1000, column=0, columnspan=3, sticky="nsew")

        prox = ttk.Button(frame, text="Proxima página", takefocus=False, command=lambda:self.proxPag(), width=self.button_width)
        prox.grid(row=1000, column=6, sticky="nsew")

        self.window.lift()#Vai fazer a janela abrir a cima de tudo
        self.window.attributes("-topmost", True)
        self.window.after_idle(self.window.attributes, '-topmost', False)

        self.window.mainloop()

    def janelaLinha(self, texto, Add_or_Del):
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

        add = ttk.Button(janela, text=texto, takefocus=False, padding=2, width=self.button_width, 
                         command=lambda:(self.atualizar_frame(cod.get(), cor.get(), qntd.get(), Add_or_Del)))
        add.grid(row=4, column=0)                                                   #Add_or_Del = True : Adiciona Linha
                                                                                   #           = False: Deleta linha
    def proxPag(self):
        print("Dar um jeito de mostrar as próximas páginas")

    def addLinha(self):
        self.janelaLinha('Add', True)

    def delLinha(self):
        self.janelaLinha('Del', False)

    
    def popUp(self, mesage):
        janela_msg = Toplevel()
        janela_msg.title("Aviso")
        janela_msg.resizable(False, False)
        janela_msg.configure(background=self.background_color)
        Label(janela_msg, text=mesage, font=self.title_font, pady=15, background=self.background_color).pack()
        Button(janela_msg, text="Fechar", font=self.text_font, command=janela_msg.destroy).pack()
    
    def atualizar_frame(self, cod, cor, qntd, Add_or_Del):#O problema ta aqui
        # Limpa o frame atual
        for i in self.window.winfo_children():
            i.destroy()
        
        if Add_or_Del == True:
            self.obj.adicionarCorNova(cod, cor, qntd)   
        else:
             self.obj.deletarCor(cod, cor, qntd)  
            
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

        #Mostra as linhas
        self.obj.consultarBanco(frame, self.font_color, self.text_font, self.background_color)

        vazio = ttk.Label(frame, text= "", font=self.text_font, foreground=self.font_color, 
                          background=self.background_color, anchor="center", padding=10)
        vazio.grid(row=999, column=0)

        add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:self.addLinha(), width=self.button_width)
        add.grid(row=1000, column=3, columnspan=3, sticky="nsew")
        
        delete = ttk.Button(frame, text="Remover linha", takefocus=False, command=lambda:self.delLinha(), width=self.button_width)
        delete.grid(row=1000, column=0, columnspan=3, sticky="nsew")

        prox = ttk.Button(frame, text="Proxima página", takefocus=False, command=lambda:self.delLinha(), width=self.button_width)
        prox.grid(row=1000, column=6, sticky="nsew")

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
                ttk.Label(window, text=f"  Código: {i[0]}", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=2, sticky="w") #Posso usar name pra chamar a label especifica
                ttk.Label(window, text=f"  Cor: {i[1]}", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=3, sticky="w")
                ttk.Label(window, text=f"  Quantidade: {i[2]}         ", font=text_font, foreground=font_color, 
                          background=background_color).grid(row=a, column=4, sticky="w")
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

    def deletarCor(self, cod, cor, qntd):
        print("Deletar do banco")
    
    def adicionarCorNova(self, cod, cor, qntd):#Vai jogar uma nova cor de linha no banco de dados
        #Verifica se o cod é um número
        try:
            # Verifica se o código é um número
            int(cod)
            
            # Verifica se a cor está correta e escrita por extenso
            if any(char.isdigit() for char in cor):
                raise ValueError
            else:      
                cor = cor.lower().strip()
            
            # Verifica se a quantidade é um número
            qntd = int(qntd)

            #Verifica se a cor já existe no banco de dados
            consulta = f"SELECT * FROM {self.nome_tabela} WHERE códigoLinha = ?"
            self.cursor.execute(consulta, (cod,))
            resultado = self.cursor.fetchone() 

            if resultado is None:
                self.cursor.execute("INSERT INTO linhas VALUES (?, ?, ?)", (cod, cor, qntd))
                self.banco.commit()
                print("Adicionado no banco")
            else:
                resultado = list(resultado)
                qntdFinal = resultado[2] + qntd

                                #UPDATE é pra atualizar uma linha da database
                self.cursor.execute("UPDATE linhas SET qntd = ? WHERE códigoLinha = ?  ", (qntdFinal, cod, ))
                self.banco.commit()
                print("Atualizado")

        except ValueError:
            super().popUp(mesage="Insira um número válido em código ou quantidade!\nOu se a cor esta escrita por extenso")
        except AttributeError:
            super().popUp(mesage="Escreva a cor por extenso!")


if __name__ == '__main__':
    app = Window(15, "#b4dff0", "#030608", "Helvetica 15 bold", "consolas 12 bold")
    
