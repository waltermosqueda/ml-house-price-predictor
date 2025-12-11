import sqlite3
import csv
import os
from datetime import datetime
from colorama import init, Fore, Style

# Inicializar colorama para colores en la consola
init(autoreset=True)

# Definición de colores estilo "neón"
NEON_BLUE = Style.BRIGHT + Fore.CYAN
NEON_GREEN = Style.BRIGHT + Fore.GREEN
NEON_YELLOW = Style.BRIGHT + Fore.YELLOW
NEON_RED = Style.BRIGHT + Fore.RED
NEON_MAGENTA = Style.BRIGHT + Fore.MAGENTA

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

def orion_titulo():
    """Imprime el título del sistema."""
    print(f"\n\n{NEON_BLUE}{'*' * 65}")
    print(f"                  🌟✨ {NEON_YELLOW}ORION✨🌟                  ")
    print(f"{NEON_BLUE}{'*' * 65}")

def bienvenida():
    """Muestra un mensaje de bienvenida al usuario."""
    orion_titulo()
    print(f"\n{Fore.GREEN}⚡ Bienvenido al Sistema de Gestión de Productos ORION ⚡\n")
    print(f"{NEON_BLUE}{'*' * 65}\n")

def despedida():
    """Muestra un mensaje de despedida y agradecimiento al salir del sistema."""
    orion_titulo()
    print(f"{NEON_RED}          🚀 Saliendo del sistema ORION...")
    print(f"{Fore.BLACK}     👋 ¡Gracias por usar nuestro servicio!👋")
    print(f" {NEON_BLUE}       Contactos: waltermosqueda86@gmail.com ")
    print(f"{NEON_GREEN}           © 2024 TALENTO TECH C24215")
    print(f"{NEON_BLUE}{'*' * 65}\n")

def agregar_producto():
    """Permite al usuario agregar un producto al inventario."""
    nombre = input(f"\n{NEON_YELLOW}Ingresá el nombre del producto: {Style.RESET_ALL}").strip()
    if not nombre:
        print(f"{NEON_RED}Error: El nombre no puede estar vacío.\n")
        return

    descripcion = input(f"{NEON_YELLOW}Ingresá la descripción: {Style.RESET_ALL}").strip()
    
    try:
        cantidad = int(input(f"{NEON_YELLOW}Ingresá la cantidad: {Style.RESET_ALL}").strip())
        if cantidad < 0:
            print(f"{NEON_RED}Error: La cantidad no puede ser negativa.\n")
            return
    except ValueError:
        print(f"{NEON_RED}Error: La cantidad debe ser un número válido.\n")
        return

    try:
        precio = float(input(f"{NEON_YELLOW}Ingresá el precio: {Style.RESET_ALL}").strip())
        if precio < 0:
            print(f"{NEON_RED}Error: El precio no puede ser negativo.\n")
            return
    except ValueError:
        print(f"{NEON_RED}Error: El precio debe ser un número válido.\n")
        return

    categoria = input(f"{NEON_YELLOW}Ingresá la categoría: {Style.RESET_ALL}").strip()
    if not categoria:
        print(f"{NEON_RED}Error: La categoría no puede estar vacía.\n")
        return

    try:
        cursor.execute(''' 
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?) 
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print(f"{NEON_GREEN}Producto agregado exitosamente.\n")
    except sqlite3.Error as e:
        print(f"{NEON_RED}Error al agregar el producto: {e}\n")

def mostrar_productos():
    """Lista todos los productos del inventario ordenados alfabéticamente por nombre."""
    cursor.execute('SELECT * FROM productos ORDER BY nombre ASC')
    productos = cursor.fetchall()

    if productos:
        print(f"\n{NEON_BLUE}Inventario de productos:\n")
        print(f"{'ID':<5} | {'Nombre':<20} | {'Descripción':<35} | {'Cantidad':<10} | {'Precio':<10} | {'Categoría':<15}")
        print('-' * 100)
        
        for p in productos:
            descripcion = p[2]
            if len(descripcion) > 35:
                descripcion = descripcion[:32] + '...'
            print(f"{p[0]:<5} | {p[1]:<20} | {descripcion:<35} | {p[3]:<10} | {p[4]:<10.2f} | {p[5]:<15}")
        print()
    else:
        print(f"{NEON_RED}No hay productos en el inventario.\n")

def actualizar_producto():
    """Permite actualizar todos los campos o solo la cantidad de un producto mediante su ID."""
    try:
        id_producto = int(input(f"\n{NEON_YELLOW}Ingresá el ID del producto a actualizar: {Style.RESET_ALL}").strip())
    except ValueError:
        print(f"{NEON_RED}Error: El ID debe ser un número válido.\n")
        return

    cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    producto = cursor.fetchone()

    if producto:
        print(f"\n{NEON_BLUE}Datos actuales del producto (ID: {producto[0]}):\n")
        print(f"Nombre: {producto[1]}")
        print(f"Descripción: {producto[2]}")
        print(f"Cantidad: {producto[3]}")
        print(f"Precio: {producto[4]}")
        print(f"Categoría: {producto[5]}")
        
        print(f"\n{NEON_GREEN}Seleccioná una opción para actualizar:\n")
        print(f"{NEON_BLUE}1. Actualizar cantidad.")
        print(f"{NEON_BLUE}2. Actualizar las características.\n")

        opcion = input(f"{NEON_YELLOW}Opción: {Style.RESET_ALL}").strip()

        if opcion == "1":
            try:
                cantidad = int(input(f"{NEON_YELLOW}Nueva cantidad: {Style.RESET_ALL}").strip())
                if cantidad < 0:
                    print(f"{NEON_RED}Error: La cantidad no puede ser negativa.\n")
                    return
                cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (cantidad, id_producto))
            except ValueError:
                print(f"{NEON_RED}Error: La cantidad debe ser un número válido.\n")
                return
        elif opcion == "2":
            nombre = input(f"\n{NEON_YELLOW}Nuevo nombre (dejar vacío para no cambiar): {Style.RESET_ALL}") or producto[1]
            descripcion = input(f"{NEON_YELLOW}Nueva descripción (dejar vacío para no cambiar): {Style.RESET_ALL}") or producto[2]

            try:
                cantidad = input(f"{NEON_YELLOW}Nueva cantidad (dejar vacío para no cambiar): {Style.RESET_ALL}")
                cantidad = int(cantidad) if cantidad else producto[3]
                if cantidad < 0:
                    print(f"{NEON_RED}Error: La cantidad no puede ser negativa.\n")
                    return
            except ValueError:
                cantidad = producto[3]

            try:
                precio = input(f"{NEON_YELLOW}Nuevo precio (dejar vacío para no cambiar): {Style.RESET_ALL}")
                precio = float(precio) if precio else producto[4]
                if precio < 0:
                    print(f"{NEON_RED}Error: El precio no puede ser negativo.\n")
                    return
            except ValueError:
                precio = producto[4]

            categoria = input(f"{NEON_YELLOW}Nueva categoría (dejar vacío para no cambiar): {Style.RESET_ALL}") or producto[5]

            cursor.execute(''' 
            UPDATE productos 
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ? 
            WHERE id = ?
            ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))

        conexion.commit()
        print(f"\n{NEON_GREEN}Producto actualizado exitosamente.\n")
    else:
        print(f"{NEON_RED}No se encontró un producto con ID {id_producto}.\n")

def eliminar_producto():
    """Permite eliminar un producto del inventario por su ID."""
    try:
        id_producto = int(input(f"{NEON_YELLOW}Ingresá el ID del producto a eliminar: {Style.RESET_ALL}").strip())
    except ValueError:
        print(f"{NEON_RED}Error: El ID debe ser un número válido.\n")
        return

    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conexion.commit()
    print(f"{NEON_GREEN}Producto eliminado exitosamente.\n")

def buscar_producto():
    """Permite buscar productos por nombre o ID en el inventario, incluyendo descripción y categoría dentro del campo nombre."""
    try:
        criterio = input(f"\n{NEON_YELLOW}Ingresá nombre, ID o palabra clave : {Style.RESET_ALL}").strip()
        cursor.execute('SELECT * FROM productos WHERE nombre LIKE ? OR id = ? OR descripcion LIKE ? OR categoria LIKE ?', 
                       ('%' + criterio + '%', criterio, '%' + criterio + '%', '%' + criterio + '%'))
    except ValueError:
        print(f"{NEON_RED}Error: Ingreso no válido.\n")
        return

    productos = cursor.fetchall()

    if productos:
        print(f"\n{NEON_BLUE}Productos encontrados:\n")
        print(f"{'ID':<5} | {'Nombre':<20} | {'Descripción':<35} | {'Cantidad':<10} | {'Precio':<10} | {'Categoría':<15}")
        print('-' * 100)

        for p in productos:
            descripcion = p[2] if len(p[2]) <= 35 else p[2][:32] + '...'
            print(f"{p[0]:<5} | {p[1]:<20} | {descripcion:<35} | {p[3]:<10} | {p[4]:<10.2f} | {p[5]:<15}")
        print()
    else:
        print(f"{NEON_RED}No se encontraron productos.\n")

def reporte_bajo_stock():
    """Genera un informe de productos con stock bajo según un límite dado."""
    try:
        limite = int(input(f"{NEON_YELLOW}Ingresá el límite de stock para el reporte: {Style.RESET_ALL}").strip())
        if limite < 0:
            print(f"{NEON_RED}Error: El límite no puede ser negativo.\n")
            return
    except ValueError:
        print(f"{NEON_RED}Error: El límite debe ser un número válido.\n")
        return

    cursor.execute('SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad ASC', (limite,))
    productos = cursor.fetchall()

    if productos:
        print(f"\n{NEON_BLUE}Productos con stock menor o igual a {limite}:\n")
        print(f"{'ID':<5} | {'Nombre':<20} | {'Descripción':<35} | {'Cantidad':<10} | {'Precio':<10} | {'Categoría':<15}")
        print('-' * 100)
        for p in productos:
            descripcion = p[2]
            if len(descripcion) > 35:
                descripcion = descripcion[:32] + '...'
            print(f"{p[0]:<5} | {p[1]:<20} | {descripcion:<35} | {p[3]:<10} | {p[4]:<10.2f} | {p[5]:<15}")
        print()
    else:
        print(f"{NEON_RED}No hay productos con stock bajo.\n")

def exportar_csv():
    """Exporta los productos del inventario a un archivo CSV en la misma carpeta que el script."""
    print(f"\n{NEON_GREEN}¿Qué tipo de reporte deseas exportar?\n")
    print(f"{NEON_BLUE}1. Lista completa de productos.")
    print(f"{NEON_BLUE}2. Productos con stock bajo.")
    print(f"{NEON_BLUE}3. Exportar productos seleccionados por nombre o palabra clave.")

    opcion = input(f"\n{NEON_YELLOW}Seleccioná una opción (1-3): {Style.RESET_ALL}").strip()

    if opcion == "1":
        cursor.execute('SELECT * FROM productos')
    elif opcion == "2":
        reporte_bajo_stock()
    elif opcion == "3":
        criterio = input(f"\n{NEON_YELLOW}Ingresá el nombre del producto o palabra clave: {Style.RESET_ALL}").strip()
        cursor.execute('SELECT * FROM productos WHERE nombre LIKE ? OR descripcion LIKE ? OR categoria LIKE ?', 
                       ('%' + criterio + '%', '%' + criterio + '%', '%' + criterio + '%'))
    else:
        print(f"{NEON_RED}Opción no válida.\n")
        return

    productos = cursor.fetchall()

    if productos:
        carpeta_proyecto = os.path.dirname(os.path.abspath(__file__))
        archivo_csv = os.path.join(carpeta_proyecto, f'reporte_inventario_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')

        with open(archivo_csv, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nombre', 'Descripción', 'Cantidad', 'Precio', 'Categoría'])
            writer.writerows(productos)

        print(f"\n{NEON_BLUE}Los productos han sido exportados a:{Fore.RED} {archivo_csv}\n")
    else:
        print(f"{NEON_RED}No hay productos para exportar.\n")


def menu():
    """Despliega el menú principal del sistema y ejecuta las opciones seleccionadas."""
    bienvenida()
    while True:
        print(f"{NEON_GREEN}Menú de Gestión de Productos ORION\n")
        print(f"{NEON_BLUE}1. Agregar producto")
        print(f"{NEON_BLUE}2. Mostrar productos")
        print(f"{NEON_BLUE}3. Actualizar producto")
        print(f"{NEON_BLUE}4. Eliminar producto")
        print(f"{NEON_BLUE}5. Buscar producto")
        print(f"{NEON_BLUE}6. Generar reporte de bajo stock")
        print(f"{NEON_BLUE}7. Exportar a CSV")
        print(f"{NEON_BLUE}8.{Fore.BLACK} Salir\n")
        opcion = input(f"{NEON_GREEN}Seleccioná una opción (1-8): {Style.RESET_ALL}").strip()

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            exportar_csv()
        elif opcion == "8":
            despedida()
            break
        else:
            print(f"{NEON_RED}Opción no válida. Intenta nuevamente.\n")

# Iniciar el menú principal
menu()

# Cerrar la conexión a la base de datos al finalizar el programa
conexion.close()
