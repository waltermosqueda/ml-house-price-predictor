import sqlite3
import csv
import os
from datetime import datetime

# Conexión a la base de datos SQLite
conexion = sqlite3.connect('inventario.db')
cursor = conexion.cursor()

# Crear la tabla 'productos' si no existe
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
)
''')

def agregar_producto(nombre, descripcion, cantidad, precio, categoria):
    cursor.execute(''' 
    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
    VALUES (?, ?, ?, ?, ?) 
    ''', (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()

def mostrar_productos():
    cursor.execute('SELECT * FROM productos ORDER BY nombre ASC')
    return cursor.fetchall()

def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    cursor.execute(''' 
    UPDATE productos 
    SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? 
    WHERE id = ?
    ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))
    conexion.commit()

def eliminar_producto(id_producto):
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conexion.commit()

def buscar_producto(criterio):
    cursor.execute('SELECT * FROM productos WHERE nombre LIKE ? OR id = ? OR descripcion LIKE ? OR categoria LIKE ?', 
                   ('%' + criterio + '%', criterio, '%' + criterio + '%', '%' + criterio + '%'))
    return cursor.fetchall()

def reporte_bajo_stock(limite):
    cursor.execute('SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC', (limite,))
    return cursor.fetchall()

def exportar_csv(archivo_csv):
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    with open(archivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Nombre', 'Descripción', 'Cantidad', 'Precio', 'Categoría'])
        writer.writerows(productos)

# Cerrar la conexión a la base de datos al finalizar el programa
def cerrar_conexion():
    conexion.close()