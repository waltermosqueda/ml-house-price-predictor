# ═══════════════════════════════════════════════════════════════════════════
# PYTHON - GUÍA COMPLETA: DE PRINCIPIANTE A AVANZADO
# ═══════════════════════════════════════════════════════════════════════════
# Lee esto de arriba hacia abajo. Cada sección construye sobre la anterior.
# Practica cada ejemplo ejecutándolo.

print("╔" + "═"*70 + "╗")
print("║" + " "*15 + "PYTHON - BIBLIA DEL PROGRAMADOR" + " "*23 + "║")
print("╚" + "═"*70 + "╝")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 1: LO MÁS BÁSICO (Primer día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "🔰 NIVEL 1: LO MÁS BÁSICO" + "\n" + "="*70)

# 1.1 PRINT - MOSTRAR COSAS EN PANTALLA
# ====================================
print("\n1.1 PRINT - Mostrar texto:")
print("Hola Mundo")
print("¡Esto aparece en pantalla!")

# 1.2 COMENTARIOS - NOTAS PARA TI (no se ejecutan)
# =================================================
print("\n1.2 COMENTARIOS:")
# Esto es un comentario de una línea
"""
Esto es un comentario
de múltiples líneas
(entre triple comilla)
"""
print("Los comentarios no aparecen al ejecutar")

# 1.3 VARIABLES - GUARDAR INFORMACIÓN
# ====================================
print("\n1.3 VARIABLES - Guardar datos:")
nombre = "Walter"
edad = 30
dinero = 1000.50

print(f"Mi nombre es {nombre}")
print(f"Tengo {edad} años")
print(f"Me quedan ${dinero}")

# 1.4 TIPOS DE DATOS - QUÉ TIPO DE INFORMACIÓN
# ==============================================
print("\n1.4 TIPOS DE DATOS:")
texto = "Soy texto"           # STRING (texto)
numero_entero = 42            # INT (número entero)
numero_decimal = 3.14         # FLOAT (número con decimales)
es_verdad = True              # BOOLEAN (Verdadero/Falso)

print(f"Texto: {texto} (tipo: {type(texto).__name__})")
print(f"Número entero: {numero_entero} (tipo: {type(numero_entero).__name__})")
print(f"Número decimal: {numero_decimal} (tipo: {type(numero_decimal).__name__})")
print(f"Booleano: {es_verdad} (tipo: {type(es_verdad).__name__})")

# 1.5 OPERACIONES BÁSICAS
# =======================
print("\n1.5 OPERACIONES MATEMÁTICAS:")
suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 5
division = 20 / 4
potencia = 2 ** 3
modulo = 17 % 5  # Residuo de división

print(f"5 + 3 = {suma}")
print(f"10 - 2 = {resta}")
print(f"4 × 5 = {multiplicacion}")
print(f"20 ÷ 4 = {division}")
print(f"2^3 = {potencia}")
print(f"17 mod 5 = {modulo}")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 2: ENTRADA Y CONTROL (Segundo día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "📚 NIVEL 2: ENTRADA Y CONTROL BÁSICO" + "\n" + "="*70)

# 2.1 INPUT - PEDIR INFORMACIÓN AL USUARIO
# ==========================================
print("\n2.1 INPUT - Pedir datos al usuario:")
# respuesta = input("¿Cuál es tu nombre? ")  # (Descomentar para probar)
# print(f"Tu nombre es: {respuesta}")

print("(Ejemplo descomentar para usar input)")

# 2.2 IF/ELSE - TOMAR DECISIONES
# ================================
print("\n2.2 IF/ELSE - Decisiones:")
edad_usuario = 18

if edad_usuario >= 18:
    print("Eres mayor de edad ✓")
else:
    print("Eres menor de edad")

# 2.3 ELIF - MÁS OPCIONES
# =======================
print("\n2.3 ELIF - Múltiples opciones:")
calificacion = 75

if calificacion >= 90:
    print("Calificación: A")
elif calificacion >= 80:
    print("Calificación: B")
elif calificacion >= 70:
    print("Calificación: C")
else:
    print("Calificación: F")

# 2.4 OPERADORES DE COMPARACIÓN
# ==============================
print("\n2.4 OPERADORES DE COMPARACIÓN:")
print(f"5 > 3: {5 > 3}")      # Mayor que
print(f"5 < 3: {5 < 3}")      # Menor que
print(f"5 == 5: {5 == 5}")    # Igual que
print(f"5 != 3: {5 != 3}")    # No igual
print(f"5 >= 5: {5 >= 5}")    # Mayor o igual
print(f"5 <= 3: {5 <= 3}")    # Menor o igual

# 2.5 OPERADORES LÓGICOS
# ======================
print("\n2.5 OPERADORES LÓGICOS (AND, OR, NOT):")
print(f"True AND True: {True and True}")
print(f"True OR False: {True or False}")
print(f"NOT True: {not True}")

# Ejemplo práctico:
edad = 25
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("✓ Puedes conducir")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 3: REPETICIONES (Tercer día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "🔄 NIVEL 3: REPETICIONES (BUCLES)" + "\n" + "="*70)

# 3.1 FOR - REPETIR VARIAS VECES
# ==============================
print("\n3.1 FOR - Contar del 1 al 5:")
for i in range(1, 6):
    print(i)

# 3.2 FOR CON LISTAS
# ==================
print("\n3.2 FOR - Recorrer lista:")
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")

# 3.3 WHILE - REPETIR MIENTRAS CONDICIÓN VERDADERA
# =================================================
print("\n3.3 WHILE - Repetir mientras:")
contador = 1
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1

# 3.4 BREAK - SALIR DEL BUCLE
# ============================
print("\n3.4 BREAK - Salir del bucle:")
for i in range(1, 10):
    if i == 5:
        print("¡Llegué a 5, me voy!")
        break
    print(i)

# 3.5 CONTINUE - SALTAR ITERACIÓN
# ================================
print("\n3.5 CONTINUE - Saltar número:")
for i in range(1, 6):
    if i == 3:
        continue  # Salta el 3
    print(i)

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 4: ESTRUCTURAS DE DATOS (Cuarto día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "📦 NIVEL 4: ESTRUCTURAS DE DATOS" + "\n" + "="*70)

# 4.1 LISTAS - GUARDAR VARIOS DATOS
# =================================
print("\n4.1 LISTAS - Guardar varios datos:")
numeros = [1, 2, 3, 4, 5]
print(f"Lista: {numeros}")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Largo: {len(numeros)}")

# 4.2 OPERACIONES CON LISTAS
# ===========================
print("\n4.2 Operaciones con listas:")
numeros.append(6)  # Añadir al final
print(f"Después de append(6): {numeros}")

numeros.pop()  # Eliminar último
print(f"Después de pop(): {numeros}")

numeros.insert(0, 0)  # Insertar en posición
print(f"Después de insert(0, 0): {numeros}")

# 4.3 TUPLAS - LISTAS INMUTABLES (no cambian)
# ===========================================
print("\n4.3 TUPLAS - Como listas pero no cambian:")
coordenadas = (10, 20, 30)
print(f"Tupla: {coordenadas}")
print(f"Primera coordenada: {coordenadas[0]}")

# 4.4 DICCIONARIOS - DATOS CON ETIQUETAS
# =======================================
print("\n4.4 DICCIONARIOS - Datos con clave:")
persona = {
    "nombre": "Walter",
    "edad": 30,
    "ciudad": "Buenos Aires"
}
print(f"Persona: {persona}")
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona['edad']}")

# 4.5 CONJUNTOS (SETS) - SIN DUPLICADOS
# ======================================
print("\n4.5 CONJUNTOS - Sin elementos duplicados:")
numeros_unicos = {1, 2, 2, 3, 3, 3}
print(f"Conjunto: {numeros_unicos}")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 5: FUNCIONES (Quinto día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "⚙️ NIVEL 5: FUNCIONES" + "\n" + "="*70)

# 5.1 FUNCIÓN SIMPLE
# ==================
print("\n5.1 Función simple:")
def saludar():
    print("¡Hola!")

saludar()  # Llamar la función

# 5.2 FUNCIÓN CON PARÁMETROS
# ===========================
print("\n5.2 Función con parámetros:")
def saludar_a(nombre):
    print(f"¡Hola {nombre}!")

saludar_a("Walter")
saludar_a("María")

# 5.3 FUNCIÓN CON RETURN
# ======================
print("\n5.3 Función que devuelve valor:")
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(f"5 + 3 = {resultado}")

# 5.4 PARÁMETROS POR DEFECTO
# ===========================
print("\n5.4 Parámetros con valor por defecto:")
def mostrar_info(nombre, edad=25):
    print(f"Nombre: {nombre}, Edad: {edad}")

mostrar_info("Ana")  # Usa edad por defecto
mostrar_info("Carlos", 35)  # Especifica edad

# 5.5 MÚLTIPLES RETURNS
# =====================
print("\n5.5 Devolver múltiples valores:")
def datos_persona():
    return "Walter", 30, "Buenos Aires"

nombre, edad, ciudad = datos_persona()
print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 6: MANIPULACIÓN DE STRINGS (Sexto día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "📝 NIVEL 6: MANIPULACIÓN DE TEXTO (STRINGS)" + "\n" + "="*70)

# 6.1 OPERACIONES CON STRINGS
# ============================
print("\n6.1 Operaciones con strings:")
texto = "Hola Mundo"
print(f"Original: {texto}")
print(f"Mayúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Largo: {len(texto)}")
print(f"Contiene 'Mundo': {'Mundo' in texto}")

# 6.2 INDEXING Y SLICING
# ======================
print("\n6.2 Acceder a caracteres:")
texto = "Python"
print(f"Primer carácter: {texto[0]}")
print(f"Último carácter: {texto[-1]}")
print(f"Del 0 al 2: {texto[0:3]}")
print(f"Del 3 al final: {texto[3:]}")

# 6.3 SPLIT Y JOIN
# ================
print("\n6.3 Dividir y unir strings:")
frase = "me encanta Python"
palabras = frase.split()
print(f"Palabras: {palabras}")

reunidas = " - ".join(palabras)
print(f"Reunidas: {reunidas}")

# 6.4 F-STRINGS (INTERPOLACIÓN)
# ==============================
print("\n6.4 F-strings - Insertar variables:")
nombre = "Walter"
edad = 30
mensaje = f"{nombre} tiene {edad} años"
print(mensaje)

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 7: MANEJO DE EXCEPCIONES (Séptimo día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "🚨 NIVEL 7: MANEJO DE ERRORES" + "\n" + "="*70)

# 7.1 TRY/EXCEPT
# ==============
print("\n7.1 Try/Except - Manejar errores:")
try:
    resultado = 10 / 0  # Error: división por cero
except ZeroDivisionError:
    print("No puedes dividir por cero")

# 7.2 MÚLTIPLES EXCEPCIONES
# ==========================
print("\n7.2 Múltiples excepciones:")
try:
    numero = int("abc")  # Error: no es número
except ValueError:
    print("Eso no es un número válido")
except TypeError:
    print("Error de tipo")

# 7.3 FINALLY - SIEMPRE EJECUTAR
# ===============================
print("\n7.3 Finally - ejecutar siempre:")
try:
    resultado = 10 / 2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error")
finally:
    print("Esto siempre se ejecuta")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 8: PROGRAMACIÓN ORIENTADA A OBJETOS (Octavo día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "🏗️ NIVEL 8: PROGRAMACIÓN ORIENTADA A OBJETOS" + "\n" + "="*70)

# 8.1 CLASES Y OBJETOS
# ====================
print("\n8.1 Crear una clase:")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")

# Crear objetos (instancias)
p1 = Persona("Walter", 30)
p2 = Persona("María", 25)

p1.presentarse()
p2.presentarse()

# 8.2 ATRIBUTOS Y MÉTODOS
# =======================
print("\n8.2 Atributos y métodos:")
class Auto:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        self.velocidad = 0
    
    def acelerar(self):
        self.velocidad += 10
    
    def estado(self):
        print(f"Auto {self.marca} {self.color} a {self.velocidad} km/h")

auto = Auto("Toyota", "Rojo")
auto.estado()
auto.acelerar()
auto.estado()

# 8.3 HERENCIA
# ============
print("\n8.3 Herencia - Clases que heredan de otras:")
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

perro = Perro("Rex")
gato = Gato("Misi")

perro.hacer_sonido()
gato.hacer_sonido()

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 9: TRABAJAR CON ARCHIVOS (Noveno día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "📁 NIVEL 9: TRABAJAR CON ARCHIVOS" + "\n" + "="*70)

# 9.1 LEER ARCHIVO
# ================
print("\n9.1 Leer archivo:")
# with open('archivo.txt', 'r') as archivo:
#     contenido = archivo.read()
#     print(contenido)
print("(Ejemplo de lectura descomentar)")

# 9.2 ESCRIBIR ARCHIVO
# ====================
print("\n9.2 Escribir archivo:")
# with open('nuevo.txt', 'w') as archivo:
#     archivo.write("Hola, esto es nuevo")
print("(Ejemplo de escritura descomentar)")

# 9.3 AÑADIR A ARCHIVO
# ====================
print("\n9.3 Añadir contenido:")
# with open('archivo.txt', 'a') as archivo:
#     archivo.write("\nNueva línea")
print("(Ejemplo de append descomentar)")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 10: LIBRERÍAS Y MÓDULOS (Décimo día)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "📚 NIVEL 10: LIBRERÍAS Y MÓDULOS" + "\n" + "="*70)

# 10.1 IMPORTAR LIBRERÍAS
# =======================
print("\n10.1 Importar librerías:")
import math
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")

# 10.2 DATETIME - TRABAJAR CON FECHAS
# ====================================
print("\n10.2 Trabajar con fechas:")
from datetime import datetime
ahora = datetime.now()
print(f"Ahora: {ahora}")
print(f"Año: {ahora.year}, Mes: {ahora.month}, Día: {ahora.day}")

# 10.3 RANDOM - NÚMEROS ALEATORIOS
# =================================
print("\n10.3 Números aleatorios:")
import random
numero_aleatorio = random.randint(1, 100)
print(f"Número aleatorio entre 1 y 100: {numero_aleatorio}")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 11: LIST COMPREHENSION (Avanzado)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "⚡ NIVEL 11: LIST COMPREHENSION (AVANZADO)" + "\n" + "="*70)

# 11.1 CREAR LISTAS DE FORMA CORTA
# ==================================
print("\n11.1 List Comprehension:")

# Forma normal:
cuadrados_normal = []
for i in range(1, 6):
    cuadrados_normal.append(i ** 2)

# Forma con List Comprehension:
cuadrados_corto = [i ** 2 for i in range(1, 6)]

print(f"Cuadrados: {cuadrados_corto}")

# 11.2 CON CONDICIÓN
# ==================
print("\n11.2 List Comprehension con condición:")
numeros_pares = [i for i in range(1, 11) if i % 2 == 0]
print(f"Números pares: {numeros_pares}")

# ═══════════════════════════════════════════════════════════════════════════
# NIVEL 12: LAMBDAS Y MAP/FILTER (Muy Avanzado)
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "🎯 NIVEL 12: LAMBDAS Y FUNCIONES DE ORDEN SUPERIOR" + "\n" + "="*70)

# 12.1 FUNCIONES LAMBDA
# =====================
print("\n12.1 Funciones lambda (funciones anónimas):")
sumar = lambda x, y: x + y
print(f"Lambda sumar(5, 3): {sumar(5, 3)}")

# 12.2 MAP - APLICAR FUNCIÓN A LISTA
# ===================================
print("\n12.2 MAP - Aplicar función a cada elemento:")
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrados con map: {cuadrados}")

# 12.3 FILTER - FILTRAR ELEMENTOS
# ================================
print("\n12.3 FILTER - Filtrar elementos:")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares con filter: {pares}")

# ═══════════════════════════════════════════════════════════════════════════
# RESUMEN FINAL
# ═══════════════════════════════════════════════════════════════════════════

print("\n" + "="*70)
print("RESUMEN VISUAL - LO QUE APRENDISTE")
print("="*70)

resumen = """
NIVEL 1: Básico
├─ print()         : Mostrar en pantalla
├─ variables       : Guardar datos
├─ tipos de datos  : int, float, str, bool
└─ operaciones     : +, -, *, /, %, **

NIVEL 2: Control
├─ if/else/elif    : Tomar decisiones
├─ comparadores    : >, <, ==, !=, >=, <=
└─ lógicos         : and, or, not

NIVEL 3: Bucles
├─ for             : Repetir N veces
├─ while           : Repetir mientras condición
├─ break           : Salir del bucle
└─ continue        : Saltar iteración

NIVEL 4: Estructuras de Datos
├─ listas []       : Guardar múltiples datos (mutables)
├─ tuplas ()       : Como listas pero inmutables
├─ dict {}         : Datos con clave-valor
└─ sets {}         : Datos sin duplicados

NIVEL 5: Funciones
├─ def             : Definir función
├─ parámetros      : Recibir datos
├─ return          : Devolver datos
└─ valores default : Parámetros opcionales

NIVEL 6: Strings
├─ upper/lower     : Mayúsculas/minúsculas
├─ indexing        : Acceder por posición
├─ slicing         : Obtener rango
├─ split/join      : Dividir/unir
└─ f-strings       : Insertar variables

NIVEL 7: Excepciones
├─ try/except      : Capturar errores
├─ finally         : Ejecutar siempre
└─ tipos de error  : ValueError, TypeError, ZeroDivisionError

NIVEL 8: Orientación a Objetos
├─ clases          : Crear objetos personalizados
├─ __init__        : Constructor
├─ self            : Referencia al objeto
├─ métodos         : Funciones del objeto
└─ herencia        : Clases que heredan de otras

NIVEL 9: Archivos
├─ open()          : Abrir archivo
├─ read/write      : Leer/escribir
└─ with            : Usar archivo seguramente

NIVEL 10: Librerías
├─ import          : Importar librería
├─ math            : Operaciones matemáticas
├─ datetime        : Trabajar con fechas
└─ random          : Números aleatorios

NIVEL 11: List Comprehension
└─ [x for x in lista] : Crear listas de forma corta

NIVEL 12: Avanzado
├─ lambda          : Funciones anónimas cortas
├─ map()           : Aplicar función a lista
└─ filter()        : Filtrar elementos

ATAJOS Y TRUCOS IMPORTANTES:
═══════════════════════════════════════════════════════════════════════════

1. F-STRINGS (RECOMENDADO):
   nombre = "Walter"
   edad = 30
   print(f"{nombre} tiene {edad} años")

2. UNPACKING (DESEMPACAR):
   a, b, c = [1, 2, 3]
   x, *resto = [1, 2, 3, 4, 5]

3. OPERADOR TERNARIO:
   resultado = "Si" if condicion else "No"

4. DICT/LIST GET:
   persona.get("nombre", "No existe")  # Seguro

5. ENUMERATE (ÍNDICE Y VALOR):
   for i, valor in enumerate(lista):
       print(i, valor)

6. ZIP (COMBINAR LISTAS):
   for a, b in zip([1, 2], ['a', 'b']):
       print(a, b)

7. OPERADORES AUMENTADOS:
   x += 5   (equivalente a x = x + 5)
   x -= 3
   x *= 2
   x /= 4

8. SLICING NEGATIVO:
   lista[-1]     # Último elemento
   lista[-3:]    # Últimos 3 elementos

9. IN Y NOT IN:
   if "a" in "palabra":
       print("Contiene a")

10. SORTED Y REVERSED:
    sorted([3, 1, 2])
    list(reversed([1, 2, 3]))

═══════════════════════════════════════════════════════════════════════════

ORDEN PARA APRENDER (RECOMENDADO):
1. Aprende NIVEL 1-3 (semana 1)
2. Aprende NIVEL 4-5 (semana 2)
3. Aprende NIVEL 6-7 (semana 3)
4. Aprende NIVEL 8-10 (semana 4)
5. Practica NIVEL 11-12 (semana 5+)

NO memorices, PRACTICA. Escribe código, ejecuta, comete errores.
Los errores son tus mejores maestros. ¡Adelante!
"""

print(resumen)

print("\n" + "="*70)
print("✓ Completaste la guía completa de Python")
print("="*70 + "\n")

print("PYTHON")
print("├─ VARIABLES: Guardar datos")
print("├─ CONDICIONALES: Tomar decisiones (if/else)")
print("├─ BUCLES: Repetir acciones (for/while)")
print("├─ FUNCIONES: Reutilizar código")
print("├─ ESTRUCTURAS: Guardar múltiples datos (listas, dicts)")
print("├─ OBJETOS: Código organizado (clases)")
print("└─ LIBRERÍAS: Código ya hecho (numpy, pandas, etc)")
