import sqlite3 as sql
from tkinter import *


banco = sql.connect(r"C:\Users\uliss\Documents\VsCode\Projetos\cadastro\cadastro.sql")
cursor = banco.cursor()

#verifica se a tabela em questão existe
nome_tabela = "cadastros"
consulta = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{nome_tabela}'"

cursor.execute(consulta)

existe = cursor.fetchone() is not None

#caso não exista a table, cria a table
if existe == False:
    cursor.execute("CREATE TABLE cadastros (usuario text, senha text)")
    banco.commit()

#acessar as informações
resultado = cursor.execute("SELECT * FROM cadastros").fetchall()

for linhas in resultado:
    print(linhas)


#janelas
def janelaCriar():
    janela = Toplevel()
    janela.configure(background="#333", padx=15, pady=15)
    Label(janela, text="Insira seu nome:", font="arial 15", fg="white", background="#333", width=20).grid(row=0, column=0)
    nome = Entry(janela, font="arial 15", width=20, background="white")
    nome.grid(row=0, column=1)
    Label(janela, text="Deverá ter de 2 a 10 letras", font="arial 10", fg="white", background="#333").grid(row=0, column=2)

    Label(janela, text="Insira a senha:", font="arial 15", fg="white", background="#333", width=20).grid(row=1, column=0)
    senha= Entry(janela, font="arial 15", width=20, background="white", show="*")
    senha.grid(row=1, column=1)
    Label(janela, text="Deverá ter de 5 a 15 caracteres", font="arial 10", fg="white", background="#333").grid(row=1, column=2)

    Button(janela, text="Criar conta", font="arial 15", fg="white", width=10, height=1, background="#333", bd=0, command=lambda:criar(nome.get(), senha.get())).grid(row=3, column=2)
    Button(janela, text="Fechar", font="arial 15", fg="white", bd=0, background='#333',command=janela.destroy).grid(row=3, column=0)
    janela.mainloop()


def errado():
    janela_criar = Toplevel()
    janela_criar.configure(background="#333")
    Label(janela_criar, text="Erro", font="arial 15", fg="white", background="#333", width=20).grid(row=0, column=0)

def certo():
    janela_criar = Toplevel()
    janela_criar.configure(background="#333")
    Label(janela_criar, text="Tudo certo", font="arial 15", fg="white", background="#333", width=20).grid(row=0, column=0)


#função para logar
def entrar(nome_, senha_):
    nome= str(nome_)
    senha = str(senha_)
    nome = nome.upper()
    consulta = "SELECT * FROM cadastros WHERE usuario=? AND senha=?"
    cursor.execute(consulta, (nome, senha))
    existe = cursor.fetchone() is not None


    if existe == True:
        certo()
    else:
        errado()

#função para criar conta
def criar(nome_, senha_):
    nome = str(nome_)
    senha = str(senha_)
    nome = nome.upper()
    consulta = "SELECT * FROM cadastros WHERE usuario=? AND senha=?"
    cursor.execute(consulta, (nome, senha))
    existe = cursor.fetchone() is not None

    if existe == False:
        if len(nome) < 3:
            errado()
        elif len(nome) > 10:
            errado()
        elif len(senha) < 5:
            errado()
        elif len(senha) > 15:
            errado()
        else:
            cursor.execute("INSERT INTO cadastros VALUES (?, ?)", (nome, senha))
            banco.commit()
            certo()
            


#Cria a janela
janela = Tk()
quadro = Frame(janela, padx=15, pady=15, background="#333", name="cadastro")
quadro.pack()

#adiciona elementos a janela
Label(quadro, text="Insira seu nome:", font="arial 15", fg="white", background="#333", width=20).grid(row=0, column=0)
nome = Entry(quadro, font="arial 15", width=20, background="white")
nome.grid(row=0, column=1)
#grid serve da mesma forma que o pack, mas é para adicionar linhas e colunas à janela

Label(quadro, text="Insira a senha:", font="arial 15", fg="white", background="#333", width=20).grid(row=1, column=0)
senha= Entry(quadro, font="arial 15", width=20, background="white", show="*")
senha.grid(row=1, column=1)
#botao de entrar
Button(quadro, text="Entrar", font="arial 15", fg="white", width=10, height=1, background="#333", bd=0, command=lambda: entrar(nome.get(), senha.get())).grid(row=3, column=1)

#botao de criar usuario
Button(quadro, text="Criar conta", font="arial 15", fg="white", width=10, height=1, background="#333", bd=0, command=lambda:janelaCriar()).grid(row=3, column=0)

#roda a janela
janela.mainloop()


