from tkinter import *
from tkinter import ttk
import func


#Tkinter começa aqui#####################################
window = Tk()
window.resizable(False, False)


window.update()#Daqui
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width*2))
y = int((screen_height/2) - (window_height*2))#até aqui é pra centralizar a janela na tela
window.geometry(f"{func.WINDOW_WIDTH}x{func.WINDOW_HEIGHT}+{x}+{y}")#aqui ajusta o tamanho e seta a janela no meio da tela

#Quadro principal
frame = Frame(window, padx= 5, pady=5, background=func.BACKGROUND_COLOR, name="gerenciador", width=func.WINDOW_WIDTH, height=func.WINDOW_HEIGHT)
frame.grid(sticky="nswe")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

title = ttk.Label(frame, text= "Gerenciador de linhas", font=func.TITLE_FONT, foreground=func.FONT_COLOR, background=func.BACKGROUND_COLOR, anchor="center", padding=10)
title.grid(row=0, column=0, columnspan=8, sticky="nsew")

add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:func.addLinha(), width=func.BUTTON_WIDTH)
add.grid(row=1, column=8, sticky="nsew")

window.mainloop()
