from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from modelo import alta as altamodelo
from modelo import borrar as borrarmodelo
import sys
print(sys.path)

# ##############################################
# VISTA
# ##############################################

root = Tk()
root.title("ALTA EMPLEADO")
        
titulo = Label(root, text="Ingrese los datos del empleado", bg="#ADD8E6", fg="black", height=1, width=60)
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

nombre = Label(root, text="Nombre")
nombre.grid(row=1, column=0, sticky=W)
apellido = Label(root, text="Apellido")
apellido.grid(row=2, column=0, sticky=W)
dni=Label(root, text="DNI")
dni.grid(row=3, column=0, sticky=W)

# Defino variables para tomar valores de campos de entrada
a_val, b_val, c_val = StringVar(), StringVar(), IntVar()
w_ancho = 20

entrada1 = Entry(root, textvariable = a_val, width = w_ancho) 
entrada1.grid(row = 1, column = 1)
entrada2 = Entry(root, textvariable = b_val, width = w_ancho) 
entrada2.grid(row = 2, column = 1)
entrada3 = Entry(root, textvariable = c_val, width = w_ancho) 
entrada3.grid(row = 3, column = 1)

# --------------------------------------------------
# TREEVIEW
# --------------------------------------------------

tree = ttk.Treeview(root)
tree["columns"]=("col1", "col2", "col3")
tree.column("#0", width=90, minwidth=50, anchor=W)
tree.column("col1", width=200, minwidth=80)
tree.column("col2", width=200, minwidth=80)
tree.column("col3", width=200, minwidth=80)
tree.heading("#0", text="Legajo")
tree.heading("col1", text="Nombre")
tree.heading("col2", text="Apellido")
tree.heading("col3", text="DNI")
tree.grid(row=10, column=0, columnspan=4)

def limpiar(nombre, apellido, dni):
    nombre.set("")
    apellido.set("")
    dni.set("")

def alta():
    retorno=altamodelo(a_val.get(), b_val.get(), c_val.get(), tree)
    limpiar(a_val, b_val, c_val)
    print(retorno)
    showinfo("Retorno", retorno)

boton_alta=Button(root, text="Alta", command=lambda:alta())
boton_alta.grid(row=6, column=1)

boton_borrar=Button(root, text="Borrar", command=lambda:borrarmodelo(tree))
boton_borrar.grid(row=8, column=1)
root.mainloop()