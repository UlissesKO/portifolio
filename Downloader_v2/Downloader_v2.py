import os
from tkinter import *
from tkinter import ttk
from pytube import YouTube
from tkinter import filedialog

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 143
BUTTON_WIDTH = 30
BACKGROUND_COLOR = "#f7f7f7"
FONT_COLOR = "#070708"
TITLE_FONT = "Helvetica 15 bold"
TEXT_FONT = "consolas 12 bold"

linkList = {}
key = 0

class Downloader:
    def __init__(self, urls, dire):
        self.urls = urls
        self.dire = dire
    
    def Download(self):
        try:
            for link in linkList:
                tuple = linkList[link]
                if tuple[1] == True and tuple[2] == False:
                    self.Download_audio(tuple[0])
                elif tuple[1] == True and tuple[2] == True:
                    self.Download_audio(tuple[0])
                    self.Download_video(tuple[0])
                else:
                    self.Download_video(tuple[0])

            popUp("Download finalizado!")
        except:
            popUp(f"Algo deu errado com a {link}ª música, tente mais tarde")

        linkList.clear()
   
    def Download_audio(self, url):
        audio = YouTube(url).streams.get_audio_only().download(self.dire) #pytube
        base, ext = os.path.splitext(audio)  #os
        arquivo_novo = base + ".mp3"
        os.rename(audio, arquivo_novo)

    def Download_video(self, url):
        YouTube(url).streams.get_highest_resolution().download(self.dire) #pytube


def addItem(entry_): #Adiciona item pra lista e apaga o texto do entry   
    global key
    global errorText
    if entry_.startswith("https://www.youtube.com/watch"):
        if isMp4.get() == False and isMp3.get() == False:
            popUp("Selecione o formato")
        else:
            linkList[key] = entry_, isMp3.get(), isMp4.get()
            key += 1
    else:
        popUp("Link inválido") 
        
    entry.delete(0, "end")

def seeQueue():#In progress
    pass

def createObj(): #Vai criar o objeto
    dire = filedialog.askdirectory()
    obj = Downloader(urls=linkList,dire=dire)
    obj.Download()

def popUp(mesage):
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.resizable(False, False)
    Label(janela_msg, text=mesage, font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()


#Tkinter começa aqui#####################################
window = Tk()
window.resizable(False, False)


window.update()#Daqui
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width*2))
y = int((screen_height/2) - (window_height*1.4))#até aqui é pra centralizar a janela na tela

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")#aqui ajusta o tamanho e seta a janela no meio da tela


#Styles do ttk
checkbuttonStyle = ttk.Style()#Estilo dos checkbuttons, pra deixar com o mesmo fundo da pagina
checkbuttonStyle.configure("Custom.TCheckbutton", background=BACKGROUND_COLOR, font=TEXT_FONT, foreground=FONT_COLOR)


frame = Frame(window, padx= 5, pady=5, background=BACKGROUND_COLOR, name="downloader", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
frame.grid()

title = ttk.Label(frame, text= "Downloader", font=TITLE_FONT, foreground=FONT_COLOR, background=BACKGROUND_COLOR, anchor="w", padding=10, width=90)
title.grid(row=0, column=0, columnspan=4, sticky="nsew")

entry = ttk.Entry(frame, text="Insira o link: ", font=TEXT_FONT, foreground=FONT_COLOR, width=60)
entry.grid(row=1, column=0, columnspan=2, sticky="we")

isMp3 = BooleanVar()
mp3 = ttk.Checkbutton(frame, text="Áudio", variable=isMp3, onvalue=True, offvalue=False, takefocus=False, padding=5, style="Custom.TCheckbutton")
mp3.grid(row=1, column=2, padx=10)

isMp4 = BooleanVar()
mp4 = ttk.Checkbutton(frame, text="Vídeo", variable=isMp4, onvalue=True, offvalue=False, takefocus=False, padding=5, style="Custom.TCheckbutton")
mp4.grid(row=2, column=2, padx=10)

add = ttk.Button(frame, text="Adicionar à fila", takefocus=False, command=lambda:addItem(entry.get()), padding=5, width=BUTTON_WIDTH)
add.grid(row=1, column=3, sticky="nsw", pady=5)

download = ttk.Button(frame, text="Baixar", takefocus=False, command=lambda:createObj(), padding=5, width=BUTTON_WIDTH)
download.grid(row=2, column=3, sticky="nsw", pady=5)

#In progress
#queue = ttk.Button(frame, text="Ver a fila", takefocus=False, command=lambda:seeQueue(), padding=5, width=BUTTON_WIDTH)
#queue.grid(row=2, column=0, sticky="we", pady=5)



window.mainloop()