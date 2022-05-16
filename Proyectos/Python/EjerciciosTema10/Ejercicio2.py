# En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

# Importing Tkinter module
import tkinter
from tkinter import *
from tkinter.ttk import *

master = Tk()

lista = ['Minecraft', 'Apex', 'League of Legends', 'Valorant', 'GTA', 'Rocket League']
lista_items = StringVar(value=lista)

listbox = tkinter.Listbox(master, listvariable=lista_items)
listbox.grid(row =1, column = 0, sticky = S)

l1 = Label(master, text = "Juegos mas jugados:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = N, pady = 2)


mainloop()