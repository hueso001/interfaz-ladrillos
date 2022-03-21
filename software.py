from tkinter import *
import tkinter as tk
from tkinter import font
from tkinter import PhotoImage
from typing import List
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog
import os

raiz = Tk()
raiz.geometry("600x600")
raiz.title("ECO-LADRILLOS")
font = ("Arial Bold", 20)
img1 = PhotoImage(file=r"./fondo/ladrillos.png")
imagen1 = img1.subsample(2)
etiquetaa = Label(raiz, bg="#f7c099", width=500, height=500).place(x=0, y=0)
etiqueta = Label(raiz, image=imagen1).place(x=100, y=30)

def clientes():
    raiz1 = Toplevel()
    raiz1.geometry("600x600")
    raiz1.title("ECO-LADRILLOS")
    font = ("Arial Bold", 20)
    etiquetaa = Label(raiz1, bg="#f7c099", width=500, height=500).place(x=0, y=0)
    pantalla = Frame(raiz1)
    pantalla.pack()

    scroll = Scrollbar(pantalla)
    scroll.pack(side=RIGHT, fill=Y)

    scroll = Scrollbar(pantalla,orient='horizontal')
    scroll.pack(side= BOTTOM,fill=X)

    tabla = ttk.Treeview(pantalla,yscrollcommand=scroll.set, xscrollcommand =scroll.set)

    tabla.pack()

    scroll.config(command=tabla.yview)
    scroll.config(command=tabla.xview)

#define our column
 
    tabla['columns'] = ('ID', 'Nombre', 'Apellido', 'Direccion', 'Telefono', "ID de pago")

# format our column
    tabla.column("#0", width=10,  stretch=NO)
    tabla.column("Nombre",anchor=NW,width=100)
    tabla.column("Apellido",anchor=NW,width=100)
    tabla.column("Direccion",anchor=NW,width=180)
    tabla.column("Telefono",anchor=NW,width=100)
    tabla.column("ID de pago",anchor=NW,width=20)

#Create Headings 
    tabla.heading("#0",text="",anchor=NW)
    tabla.heading("Nombre",text="Nombre",anchor=NW)
    tabla.heading("Apellido",text="Apellido",anchor=NW)
    tabla.heading("Direccion",text="Direccion",anchor=NW)
    tabla.heading("Telefono",text="Telefono",anchor=NW)
    tabla.heading("ID de pago",text="ID de pago",anchor=NW)

#add data 
    tabla.insert(parent='',index='end',iid=0,text='',values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=1,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=2,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=3,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=4,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=5,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=6,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=7,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=8,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=9,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.insert(parent='',index='end',iid=10,text='',
    values=("01", "Juan Carlos ","Segovia","Comandante Salas 145","+4925156871", "21"))
    tabla.pack()


    boton1 = Button(raiz1, text="Clientes", width=11, height=2).place(x=144, y=430)
    boton2 = Button(raiz1, text="Pedidos", width=11, height=2).place(x=244, y=430)
    boton3 = Button(raiz1, text="Ventas", width=11, height=2).place(x=344, y=430)

    def cierre():
        raiz1.destroy()
    tk.Button(raiz1, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)


def pedidos():
    raiz2 = Toplevel()
    raiz2.geometry("600x600")
    raiz2.title("ECO-LADRILLOS")
    font = ("Arial Bold", 20)
    etiquetaa = Label(raiz2, bg="#f7c099", width=500, height=500).place(x=0, y=0)
    pantalla = Frame(raiz2)
    pantalla.pack()

    scroll = Scrollbar(pantalla)
    scroll.pack(side=RIGHT, fill=Y)

    scroll = Scrollbar(pantalla,orient='horizontal')
    scroll.pack(side= BOTTOM,fill=X)

    tabla = ttk.Treeview(pantalla,yscrollcommand=scroll.set, xscrollcommand =scroll.set)

    tabla.pack()

    scroll.config(command=tabla.yview)
    scroll.config(command=tabla.xview)

#define our column
 
    tabla['columns'] = ('ID', 'Nombre', 'Apellido', 'Direccion', 'Telefono')

# format our column
    tabla.column("#0", width=10,  stretch=NO)
    tabla.column("Nombre",anchor=NW,width=70)
    tabla.column("Apellido",anchor=NW,width=70)
    tabla.column("Direccion",anchor=NW,width=100)
    tabla.column("Telefono",anchor=NW,width=80)



#Create Headings 
    tabla.heading("#0",text="",anchor=NW)
    tabla.heading("Nombre",text="Nro. de pedido",anchor=NW)
    tabla.heading("Apellido",text="Fecha",anchor=NW)
    tabla.heading("Direccion",text="Cantidad",anchor=NW)
    tabla.heading("Telefono",text="id de pago",anchor=NW)


#add data 
    tabla.insert(parent='',index='end',iid=0,text='',values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=1,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=2,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=3,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=4,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=5,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=6,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=7,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=8,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=9,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.insert(parent='',index='end',iid=10,text='',
    values=("01", "254 ","12/11/2021","2500","4"))
    tabla.pack()


    boton1 = Button(raiz2, text="Ingresar pedido", width=11, height=2).place(x=144, y=430)
    boton2 = Button(raiz2, text="Modificar pedido", width=15, height=2).place(x=244, y=430)
    boton3 = Button(raiz2, text="Anular pedido", width=11, height=2).place(x=374, y=430)

    def cierre():
        raiz2.destroy()
    tk.Button(raiz2, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)


def ventas():
    raiz3 = Toplevel()
    raiz3.geometry("500x350")
    raiz3.title("ECO-LADRILLOS")
    font = ("Arial Bold", 20)
    etiquetaa = Label(raiz3, bg="#f7c099", width=500, height=500).place(x=0, y=0)
    pantalla = Frame(raiz3)
    pantalla.pack()


    etiqueta1 = Label(raiz3, text="Producto", width=18, height=1, fg="black",font=("Arial Bold",15)).place(x=5, y=20)
    label_text = Entry(raiz3).place(x=220, y=20, width=200, height=30)  

    etiqueta1 = Label(raiz3, text="Forma de Pago", width=18, height=1, fg="black",font=("Arial Bold",15)).place(x=5, y=55)
    label_text = Entry(raiz3).place(x=220, y=55, width=200, height=30)  

    etiqueta1 = Label(raiz3, text="Precio total", width=18, height=1, fg="black",font=("Arial Bold",15)).place(x=5, y=90)
    label_text = Entry(raiz3).place(x=220, y=90, width=200, height=30)

    etiqueta1 = Label(raiz3, text="Fecha", width=18, height=1, fg="black",font=("Arial Bold",15)).place(x=5, y=125)
    label_text = Entry(raiz3).place(x=220, y=125, width=200, height=30)

    etiqueta1 = Label(raiz3, text="Cantidad", width=18, height=1, fg="black",font=("Arial Bold",15)).place(x=5, y=195)
    label_text = Entry(raiz3).place(x=220, y=195, width=200, height=30)

    Botones = Button(raiz3, text="Imprimir", width=15, height=2).place(x=260, y=230)
    Botones = Button(raiz3, text="Cancerlar", width=15, height=2).place(x=55, y=230)
    def cierre():
            raiz3.destroy()
    tk.Button(raiz3, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)





boton1 = Button(raiz, text="Clientes", width=11, height=2, command=clientes).place(x=144, y=430)
boton2 = Button(raiz, text="Pedidos", width=11, height=2,command=pedidos).place(x=244, y=430)
boton3 = Button(raiz, text="Ventas", width=11, height=2,command=ventas).place(x=344, y=430)

def cierre():
    raiz.destroy()
tk.Button(raiz, text="Salir", width=10, height=2, command=cierre).pack(side=BOTTOM)

raiz.mainloop()