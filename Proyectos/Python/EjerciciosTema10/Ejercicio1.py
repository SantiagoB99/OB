# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción
# que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

# Al principio no tiene que haber una opción seleccionada.

# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *

def elegir():
    texto.config(textvariable = v)

def reiniciar():
    texto.config(textvariable =" ")


# Creating master Tkinter window
master = Tk()


# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

values = {"Fortnite" : "Fortnite",
          "Valorant " : "Valorant",
          "Apex" : "Apex",
          "GTA" : "GTA",
          "Minecraft" : "Minecraft"}


for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value, command=elegir).pack(side = TOP, ipady = 5)

texto = Label(master)
texto.pack()
Button(master, text="Reiniciar", command=reiniciar).pack()

mainloop()