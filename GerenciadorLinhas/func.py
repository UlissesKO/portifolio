import sqlite3 as sql
from tkinter import *
from tkinter import ttk

BUTTON_WIDTH = 15
BACKGROUND_COLOR = "#b4dff0"
FONT_COLOR = "#030608"
TITLE_FONT = "Helvetica 15 bold"
TEXT_FONT = "consolas 12 bold"

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
    
    def consultarBanco():#Vai ver quantas linhas tem no banco, pra colocar no hud
        pass

    def alterarQntdLinha():#Vai mudar a quantidade de linhas de tal cor no banco
        pass

    def adicionarCorNova():#Vai jogar uma nova cor de linha no banco de dados
        pass
    
#Tkinter
def addLinha():
    janela = Toplevel()
    janela.configure(background=BACKGROUND_COLOR, padx=10, pady=10)

    ttk.Label(janela, text="Insira o código da linha", font=TEXT_FONT, foreground=FONT_COLOR, background=BACKGROUND_COLOR, padding=10).grid(row=0, column=0)
    cod = ttk.Entry(janela, font=TEXT_FONT, width=6, background="white")
    cod.grid(row=0, column=1)

    ttk.Label(janela, text="Escreva a cor da linha", font=TEXT_FONT, foreground=FONT_COLOR, background=BACKGROUND_COLOR, padding=10).grid(row=1, column=0)
    cor = ttk.Entry(janela, font=TEXT_FONT, width=6, background="white")
    cor.grid(row=1, column=1)

    add = ttk.Button(janela, text="Add", takefocus=False, padding=2, width=BUTTON_WIDTH)
    add.grid(row=4, column=2)#Esse botao vai chamar a função adicionarCorNova()

obj = Gerenciador("GerenciadorLinhas\linhas.sql")
