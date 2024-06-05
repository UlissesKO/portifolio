from tkinter import *
from tkinter import ttk
import func


window = Tk()
window.resizable(False, False)

frame = Frame(window, padx= 5, pady=5, background=func.BACKGROUND_COLOR, name="gerenciador")
frame.grid(sticky="nswe")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

title = ttk.Label(frame, text= "Gerenciador de linhas", font=func.TITLE_FONT, foreground=func.FONT_COLOR, background=func.BACKGROUND_COLOR, anchor="center", padding=10)
title.grid(row=0, column=0, columnspan=8, sticky="nsew")

#Vou precisar fazer algo parecido com for loop nas linhas do banco de dados pra colocar elas aqui

add = ttk.Button(frame, text="Adicionar linha", takefocus=False, command=lambda:func.addLinha(), width=func.BUTTON_WIDTH)
add.grid(row=6, column=8, sticky="nsew")

window.mainloop()
