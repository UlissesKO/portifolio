import os
from tkinter import *
from pytube import YouTube
from tkinter import filedialog


def avisoFinalErro():
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.geometry("500x100")
    Label(janela_msg, text="Arquivo já existe ou o link está incorreto", font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()


def avisoFinalErro2():
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.geometry("500x100")
    Label(janela_msg, text="Alguma coisa deu errado", font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()
    

def avisoFinal():
    janela_msg = Toplevel()
    janela_msg.title("Aviso")
    janela_msg.geometry("200x100")
    Label(janela_msg, text="Download finalizado", font="arial 14", pady=15).pack()
    Button(janela_msg, text="Fechar", font="arial 12", command=janela_msg.destroy).pack()


def downloadAudio(url_):
    url_2 = list(url_)
    try:
        if url_2[0:23] == ["h","t","t","p","s",":","/","/","w","w","w",".","y","o","u","t","u","b","e",".","c","o","m"]:
            pasta = filedialog.askdirectory() #tkinter
            audio = YouTube(url_).streams.get_audio_only().download(pasta) #pytube
            base, ext = os.path.splitext(audio)  #os

            arquivo_novo = base + ".mp3"
            os.rename(audio, arquivo_novo)

            avisoFinal()
        else:
            avisoFinalErro()
    except:
        avisoFinalErro2()


def downloadVideo(url_):
    url_2 = list(url_)
    try:
        if url_2[0:23] == ["h","t","t","p","s",":","/","/","w","w","w",".","y","o","u","t","u","b","e",".","c","o","m"]:
            pasta = filedialog.askdirectory() #tkinter
            YouTube(url_).streams.get_highest_resolution().download(pasta) #pytube

            avisoFinal()
        else:
            avisoFinalErro()
    except:
        avisoFinalErro2()


janela = Tk()#cria a window


quadro = Frame(janela, pady=15, padx=15, background="#333", name="downloader")#cria o espaço pra ui
quadro.pack()#junta tudo

Label(quadro, text="Downloader de videos do Youtube", font="arial 14", fg="white", background="#333").pack()#texto
Label(quadro, text="Insira o URL do video: ", font="arial 14", fg="white", background="#333").pack(side="left")#texto
url = Entry(quadro, font="arial 12", width=75, background="white",)#entrada de dados
url.pack(side="left")
Button(quadro, text="Download Aúdio", font="arial 10", width=15, height=1,background="#093", bd=1, fg="#000000", command= lambda: downloadAudio(url.get())).pack(side="right")
Button(quadro, text="Download Video", font="arial 10", width=15, height=1,background="#090", bd=1, fg="#000000", command= lambda: downloadVideo(url.get())).pack(side="right")

janela.mainloop()   