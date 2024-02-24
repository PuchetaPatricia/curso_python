import sqlite3
import re

# ##############################################
# MODELO
# ##############################################
def conexion():
    con = sqlite3.connect("mibase.db")
    return con

def crear_tabla():
    con = conexion()
    cursor = con.cursor()
    sql = """CREATE TABLE empleados
             (legajo INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre varchar(20) NOT NULL,
             apellido varchar(20) NOT NULL,
             dni INTEGER)
    """
    cursor.execute(sql)
    con.commit()

try:
    conexion()
    crear_tabla()
except:
    print("Hay un error")


def alta(nombre, apellido, dni, tree):
    patron="^[A-Za-záéíóú]*$"  #regex para el campo cadena
    if(re.match(patron, nombre) and re.match(patron, apellido)):
        print(nombre, apellido, dni)
        con=conexion()
        cursor=con.cursor()
        data=(nombre, apellido, dni)
        sql="INSERT INTO empleados(nombre, apellido, dni) VALUES(?, ?, ?)"
        cursor.execute(sql, data)
        con.commit()
        print("Estoy en alta todo ok")
        actualizar_treeview(tree)
        return f"Alta del empleado {nombre} {apellido} DNI: {dni}"
    else:
        print("error en campo nombre o apellido")
        return "Error en alta"


# def consultar():
#     global compra
#     print(compra)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM empleados WHERE legajo = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)



def actualizar_treeview(mitreview):
    records = mitreview.get_children()
    for element in records:
        mitreview.delete(element)

    sql = "SELECT * FROM empleados ORDER BY legajo ASC"
    con=conexion()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))
