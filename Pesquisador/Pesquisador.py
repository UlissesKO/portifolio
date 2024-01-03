from tkinter import *
import sqlite3 as sql
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


servico = Service(ChromeDriverManager().install()) #vai instalar o driver certo pra versao do navegador
navegador = webdriver.Chrome(service=servico)  #ta dizendo qual o navegador

#Banco de dados

#conecta com banco de dados
banco = sql.connect(r"C:\Users\uliss\Documents\VsCode\Projetos\Pesquisador\pesquisador.db")
cursor = banco.cursor()

#verifica existencia da table
consulta = "SELECT name FROM sqlite_master WHERE type='table' AND name='preços'"
cursor.execute(consulta) 
existe = cursor.fetchone() is not None
if existe == False:
    cursor.execute("CREATE TABLE preços (produto text, data text, preço numeric)")
    banco.commit()


#funções
def pesquisar(produto_, amazon_, mercadolivre_, pichau_, terabyte_):
    #aqui ja vai entrar o selenium
    if amazon_ == 1:
        #abre o site da amazon
        navegador.get("https://www.amazon.com.br/?ref_=icp_country_from_us")
        #digita na barra de pesquisa
        navegador.find_element("xpath", "//*[@id='twotabsearchtextbox']").send_keys(produto_)
        #aperta pra pesquisar
        navegador.find_element("xpath", "//*[@id='nav-search-submit-button']").click()
        #nome do primeiro produto
        produto1 = navegador.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[3]/div[2]/h2/a/span').text
        preço1 = navegador.find_element("xpath", '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[7]/div/div/span/div/div/div[3]/div[4]/div/div[1]/a/span/span[2]/span[2]').text
        #ta dando errado
    if mercadolivre_ == 1:
        print("mercado livre")
    if pichau_ == 1:
        print("pichau")
    if terabyte_ == 1:
        print("terabyte")
    
    

    return produto1, preço1




#janela

janela = Tk()
ui = Frame(janela, padx=5, pady=5, name="pesquisador")
ui.pack()   

#Elementos da janela
Label(ui, text="Qual o produto?", font="arial 15").pack()
produto = Entry(ui, font="arial 15", width="100", background="white")
produto.pack()

Button(ui, text="Pesquisar", font="arial 15", bd=1, command=lambda:pesquisar(produto.get(),amazon.get(), \
                                                                             mercadoLivre.get(),pichau.get(), \
                                                                                terabyte.get())).pack()
#checkboxes
amazon = IntVar()
Checkbutton(ui, text="Amazon", variable=amazon).pack(side="left")

mercadoLivre = IntVar()
Checkbutton(ui, text="Mercado Livre", variable=mercadoLivre).pack(side="left")

pichau = IntVar()
Checkbutton(ui, text="Pichau", variable=pichau).pack(side="left")

terabyte = IntVar()
Checkbutton(ui, text="Terabyte", variable=terabyte).pack(side="left")




janela.mainloop()



