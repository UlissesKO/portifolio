import sqlite3 as sql
from tkinter import *
from tkinter import ttk

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700
BUTTON_WIDTH = 15
BACKGROUND_COLOR = "#b4dff0"
FONT_COLOR = "#030608"
TITLE_FONT = "Helvetica 15 bold"
TEXT_FONT = "consolas 12 bold"

class Gerenciador():
    def __init__(self, path):
        self.path = path
        
        self.banco = sql.connect("GerenciadorLinhas\linhas.sql")
        self.cursor = self.banco.cursor()

        #verifica se a tabela em questão existe
        nome_tabela = "linhas"
        consulta = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nome_tabela}'"
        self.cursor.execute(consulta)
        existe = self.cursor.fetchone() is not None

        if existe == False:
            self.cursor.execute("CREATE TABLE cadastros (códigoLinha, corLinha, qntd)")
            self.banco.commit()
    
    def consultarBanco():
        pass

    def adicionarLinha():
        pass
    
#Tkinter
def addLinha():
    janela = Toplevel()
    janela.configure(background=BACKGROUND_COLOR, padx=10, pady=10)

    ttk.Label(janela, text="Insira o código da linha", font=TEXT_FONT, foreground=FONT_COLOR, background=BACKGROUND_COLOR, padding=10).grid(row=0, column=0)
    cod = ttk.Entry(janela, font=TEXT_FONT, width=6, background="white")
    cod.grid(row=0, column=1)

