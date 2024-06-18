import sqlite3 as sql
from tkinter import *
from tkinter import ttk
from tkinter import filedialog




class Gerenciador():
    def __init__(self, path):
        self.path = path
        
        self.banco = sql.connect(path)
        self.cursor = self.banco.cursor()


        #verifica se a tabela em questão existe
        nome_tabela = "linhas"
        consulta = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nome_tabela}'"
        self.cursor.execute(consulta)
        existe = self.cursor.fetchone() is not None

        if existe == False:
            self.cursor.execute("CREATE TABLE linhas (códigoLinha, corLinha, qntd)")
            self.banco.commit()
        else:
            pass

    
    def consultarBanco(self):#Vai ver quantas linhas tem no banco, pra colocar no hud
        pass

    def alterarQntdLinha(self):#Vai mudar a quantidade de linhas de tal cor no banco
        pass

    def adicionarCorNova(self, cod, cor, qntd):#Vai jogar uma nova cor de linha no banco de dados
        pass

class Window():
    def __init__(self, button_width, background_color, font_color, title_font, text_font):
        self.button_width = button_width
        self.background_color = background_color
        self.font_color = font_color
        self.title_font = title_font
        self.text_font = text_font
    
    def createDB(self): #Vai iniciar o banco de dados
        path = ""

        while path == "":
            path = filedialog.askopenfilename(
            title="Selecione um arquivo",
            filetypes=[("Arquivos SQL", "*.sql")]
            ) 
        self.obj = Gerenciador(path)
        self.main()

    def main(self):
        window = Tk()
        window.resizable(False, False)

        frame = Frame(window, padx= 5, pady=5, background=self.background_color, name="gerenciador")
        frame.grid(sticky="nswe")

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        title = ttk.Label(frame, text= "Gerenciador de linhas", font=self.title_font, foreground=self.font_color, background=self.background_color, anchor="center", padding=10)
        title.grid(row=0, column=0, columnspan=8, sticky="nsew")

        #Vou precisar fazer algo parecido com for loop nas linhas do banco de dados pra colocar elas aqui

        add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:self.addLinha(), width=self.button_width)
        add.grid(row=6, column=8, sticky="nsew")

        window.lift()#Vai fazer a janela abrir a cima de tudo
        window.attributes("-topmost", True)
        window.after_idle(window.attributes, '-topmost', False)

        window.mainloop()

    def addLinha(self):
        janela = Toplevel()
        janela.configure(background=self.background_color, padx=10, pady=10)

        ttk.Label(janela, text="Insira o código da linha", font=self.text_font, foreground=self.font_color, background=self.background_color, padding=10).grid(row=0, column=0)
        cod = ttk.Entry(janela, font=self.text_font, width=10)
        cod.grid(row=0, column=1)

        ttk.Label(janela, text="Escreva a cor da linha", font=self.text_font, foreground=self.font_color, background=self.background_color, padding=10).grid(row=1, column=0)
        cor = ttk.Entry(janela, font=self.text_font, width=10)
        cor.grid(row=1, column=1)

        ttk.Label(janela, text="Quantos cones tem?", font=self.text_font, foreground=self.font_color, background=self.background_color, padding=10).grid(row=2, column=0)
        qntd = ttk.Entry(janela, font=self.text_font, width=10)
        qntd.grid(row=2, column=1) 

        add = ttk.Button(janela, text="Add", takefocus=False, padding=2, width=self.button_width, 
                         command=lambda:self.obj.adicionarCorNova(cod.get(), cor.get(), qntd.get()))
        add.grid(row=4, column=0)#Esse botao vai chamar a função adicionarCorNova()


app = Window(15, "#b4dff0", "#030608", "Helvetica 15 bold", "consolas 12 bold")
app.createDB()


