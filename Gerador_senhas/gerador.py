import cryptocode as cry
from tkinter import *
from tkinter import ttk
import random
import sqlite3 as sql
import os


BACKGROUND_COLOR = "#000033"
BACKGROUND_TITLE_COLOR = "#003366"
BUTTON_COLOR = "#6699FF"
FONT_COLLOR = "#FFFFFF"
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 320


ACTUAL_DIRECTORY = os.path.dirname(__file__)
DATA_BASE_WAY = os.path.join(ACTUAL_DIRECTORY, 'gerador.sql')
DATA_BASE = sql.connect(DATA_BASE_WAY)
CURSOR = DATA_BASE.cursor()



class main:
    def __init__(self, user, keyPassword, keyUser,keySite, site, capitalize, lowercase, specialChar, numbers, size):
        self.user = user
        self.keyPassword = keyPassword
        self.keyUser = keyUser
        self.keySite = keySite
        self.site = site
        self.capitalize = capitalize
        self.lowercase = lowercase
        self.specialChar = specialChar
        self.numbers = numbers
        self.size = size
        
        self.strPassword = ""
        self.cryptoPassword = ""
        self.cryptoUser = ""
        self.cryptoSite =""

        self.booleanCap = BooleanVar()
        self.booleanLow = BooleanVar()
        self.booleanChar = BooleanVar()
        self.booleanNum = BooleanVar()
        self.booleanSize = BooleanVar()

        self.listLower = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","t","u","v","w","x","y","z")
        self.listCapitalize = (i.upper() for i in self.listLower)
        self.listNumbers = ("0","1","2","3","4","5","6","7","8","9")
        self.listChar = ("!","@","#","$","%","7","*","-","_","=","+")
        self.list = []

    def setOption(self):

        passwordSaved = ""

        if self.capitalize == 1:
            for i in self.listCapitalize:
                self.list.append(i)
        else:
            pass
        if self.lowercase == 1:
            for i in self.listLower:
                self.list.append(i)
        else:
            pass
        if self.specialChar == 1:
            for i in self.listNumbers:
                self.list.append(i)
        else:
            pass
        if self.numbers == 1:
            for i in self.listChar:
                self.list.append(i)
        else:
            pass
        
        self.size = int(self.size)

        self.createPassword()

    def createPassword(self):#gerar uma senha aleatoria com base nas preferencias. Ser acionado pela funçao setOption
        password = random.sample(self.list, self.size)
        for i in password:
            self.strPassword = self.strPassword + i

        self.cryptoData()

    def cryptoData(self):#criptografa a senha e o usuário. Ser acionado pela funçao createPassword
        self.cryptoPassword = cry.encrypt(self.strPassword, self.keyPassword)
        self.cryptoUser = cry.encrypt(self.user, self.keyUser)
        self.cryptoSite = cry.encrypt(self.site, self.keySite)

        self.savePassword()      

    def savePassword(self):#mandar pro banco de dados. Ser acionado pela funçao cryptoData
        verify()
        CURSOR.execute("INSERT INTO Passwords VALUES (?, ?, ?)", (self.cryptoPassword, self.cryptoUser, self.cryptoSite))
        DATA_BASE.commit()


def acessPassword():#pegar senha e o usuario do banco de dados e descriptografar. Ser acionado pela tab2
    try:
        show = CURSOR.execute("SELECT * FROM Passwords")
        a = 1
        for i in show:
            decryptedPassword = cry.decrypt(i[0], keyPassword)
            ttk.Label(tab2, text=decryptedPassword, font="consolas 12", foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=a, column=1)
            decryptedUser = cry.decrypt(i[1], keyUser)
            ttk.Label(tab2, text=decryptedUser, font="consolas 12", foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=a, column=2)
            decryptedSite = cry.decrypt(i[2], keySite)
            ttk.Label(tab2, text=decryptedSite, font="consolas 12", foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=a, column=3)
            a += 1
            
    except:
        ttk.Label(tab2, text="Ainda não tem nenhuma senha salva",font="consolas 12", foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=1, column=1)

keyPassword="TU-Tu_tU_-_ru="
keyUser="_-=Max-_=.,Verstappen_;"
keySite="MAx_-mAX,MAX-_+=SupERMAX"

def getData(): #coleta todos os dados e verifica se tem algum campo em branco
        obj = main(user.get(), keyPassword, keyUser, keySite, site.get(), capitalizeValue.get(), lowerValue.get(), \
                   charsValue.get(), numbersValue.get(), sizeBaseValue.get())
        list = [capitalizeValue.get(), lowerValue.get(), charsValue.get(), numbersValue.get()]
        list2 = [user.get(), site.get()]
        if not all (i == 0  or "" for i in list):
            if "" in list2:
                avisoFinalErro()
            else:
                if sizeBaseValue.get() == "Quantos caracteres?":
                    avisoFinalErro()
                else:
                    obj.setOption()
        else:
            avisoFinalErro()

def avisoFinalErro(): #Janela de erro
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.geometry("500x100")
    Label(janela_msg, text="Esta faltando informações", font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()

def verify(): #verifica se a table existe, caso não exista cria a table
    tableName = "Passwords"
    verify = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{tableName}'"
    CURSOR.execute(verify)
    exists = CURSOR.fetchone() is not None
    if exists == False:
        CURSOR.execute(f"CREATE TABLE {tableName} (password text, user text, site text)")
        DATA_BASE.commit()



window = Tk()
window.resizable(False,False)#não pode mudar o tamanho

#Styles do ttk
checkbuttonStyle = ttk.Style()#Estilo dos checkbuttons, pra deixar com o mesmo fundo da pagina
checkbuttonStyle.configure("Custom.TCheckbutton", background=BACKGROUND_COLOR, font=("consolas 12"), foreground=FONT_COLLOR)


window.update()#Daqui
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width*2))
y = int((screen_height/2) - (window_height*1.4))#até aqui é pra centralizar a janela na tela


window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")#aqui ajusta o tamanho e seta a janela no meio da tela


notebook = ttk.Notebook(window, height=WINDOW_HEIGHT, width=WINDOW_WIDTH, padding=-2)#tipo as abas do google
tab1 = Frame(notebook, background=BACKGROUND_COLOR)#Pra cada guia tem criar um frame novo
tab2 = Frame(notebook, background=BACKGROUND_COLOR)

#Primeira guia
notebook.add(tab1, text="Gerar novas senhas", padding=-1)
title = ttk.Label(tab1, text="Gerador de senhas", font="Helvetica 15 bold", foreground=FONT_COLLOR, background=BACKGROUND_TITLE_COLOR, anchor="center", padding=5, width=83)
title.grid(row=0, column=0, columnspan=3, sticky="nsew")#pra fazer ocupar todo o espaço
                            #pra ocupar uma linha inteira
ttk.Label(tab1, text="Insira o usuário:", font="consolas 12 bold",padding=10,foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=1, column=0)
user = ttk.Entry(tab1, font="consola 12")
user.grid(row=1, column=1, columnspan=2, sticky="ew")

ttk.Label(tab1, text="Insira o site:", font="consolas 12 bold", padding=10, foreground=FONT_COLLOR, background=BACKGROUND_COLOR).grid(row=2, column=0)
site = ttk.Entry(tab1, font="consola 12")
site.grid(row=2, column=1, columnspan=2, sticky="ew")


ttk.Separator(tab1, orient="horizontal").grid(row=4, columnspan=4, sticky="nwes")
ttk.Label(tab1, text="Opções de aleatorização:", font="Helvetica 12 bold", foreground=FONT_COLLOR, background=BACKGROUND_COLOR, padding=10).grid(row=5, column=0)


#tudo maiúsculo
capitalizeValue = IntVar()
capitalize = ttk.Checkbutton(tab1, text="Conter  letras maiúsculas", variable=capitalizeValue, style="Custom.TCheckbutton", \
                             takefocus=False, padding=10, offvalue=0, onvalue=1)
capitalize.grid(row=7, column=0, sticky="w")

#tudo minusculo
lowerValue = IntVar()
lower = ttk.Checkbutton(tab1, text="Conter  letras minúsculas", variable=lowerValue, style="Custom.TCheckbutton", \
                        takefocus=False, padding=10,offvalue=0, onvalue=1)
lower.grid(row=8, column=0, sticky="w")

#caracteres especiais
charsValue = IntVar()
chars = ttk.Checkbutton(tab1, text="Conter caracteres especiais", variable=charsValue, style="Custom.TCheckbutton", takefocus=False, padding=10)
chars.grid(row=7, column=1, sticky="w")

#números
numbersValue = IntVar()
numbers = ttk.Checkbutton(tab1, text="Conter números", variable=numbersValue, style="Custom.TCheckbutton", takefocus=False, padding=10)
numbers.grid(row=8, column=1, sticky="w")

#checkboxes com as opções de randomização de senhas
#Menu Dropdown quantidade de caracteres
sizeList = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sizeBaseValue = StringVar()
sizeBaseValue.set("Quantos caracteres?")
dropdown = ttk.Combobox(tab1, textvariable=sizeBaseValue, values=sizeList, font="consolas 11", width=30, state="readonly")
dropdown.grid(row=9, column=1, sticky="w") 

#botão pra gerar e salvar a senha
randomizePassword = ttk.Button(tab1, text="Gerar uma nova senha", takefocus = False, padding=5, command=lambda:getData())
randomizePassword.grid(row=9, column=2, stick="w")


#Segunda guia
notebook.add(tab2, text="Acessar minhas senhas", padding=-1)

title2 = ttk.Label(tab2, text="Acessar suas senhas", font="Helvetica 17", foreground=FONT_COLLOR, background=BACKGROUND_TITLE_COLOR, anchor="center", width=70, padding=5)
title2.grid(row=0,column=0, columnspan=4, sticky="nswe")

shower = ttk.Button(tab2, text="Mostrar", takefocus=False, padding=5, command=lambda:acessPassword())
shower.grid(row=1, column=0, sticky="sw")




notebook.grid()
window.mainloop()