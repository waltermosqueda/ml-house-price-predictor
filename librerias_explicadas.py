# ============================================
# GUÍA COMPLETA: CUÁNDO USAR CADA LIBRERÍA
# ============================================

# 1. NUMPY (np) - Para NÚMEROS y CÁLCULOS MATEMÁTICOS
# =====================================================
# ¿Cuándo usar? Cuando trabajas con números, matrices, operaciones matemáticas
# Ejemplo: sumar 1000 números, hacer cálculos científicos

import numpy as np

# Sin numpy (lento):
numeros = [1, 2, 3, 4, 5]
suma_lenta = sum(numeros)
print(f"Suma lenta: {suma_lenta}")

# Con numpy (rápido):
numeros_numpy = np.array([1, 2, 3, 4, 5])
suma_rapida = numeros_numpy.sum()
print(f"Suma rápida con numpy: {suma_rapida}")

# Operaciones matemáticas rápidas:
promedio = np.mean(numeros_numpy)
print(f"Promedio: {promedio}")

print("\n" + "="*50 + "\n")

# 2. PANDAS (pd) - Para DATOS en TABLAS (tipo Excel)
# ====================================================
# ¿Cuándo usar? Cuando tienes datos como filas y columnas (tabla)
# Ejemplo: lista de productos, inventario, reporte de ventas

import pandas as pd

# Crear una tabla de datos (como Excel)
# Columnas: nombre, cantidad, precio
datos_productos = {
    'nombre': ['Monitor', 'Teclado', 'Mouse'],
    'cantidad': [10, 25, 50],
    'precio': [555.0, 150.0, 80.0]
}

# Convertir a tabla (DataFrame) con pandas
tabla = pd.DataFrame(datos_productos)
print("Tabla de productos:")
print(tabla)
print()

# Operaciones útiles con pandas:
print(f"Cantidad total de productos: {tabla['cantidad'].sum()}")
print(f"Precio promedio: {tabla['precio'].mean()}")
print(f"Producto más caro: {tabla['precio'].max()}")

print("\n" + "="*50 + "\n")

# 3. MATPLOTLIB (plt) - Para GRÁFICOS y VISUALIZACIÓN
# =====================================================
# ¿Cuándo usar? Cuando quieres ver datos en forma de gráficos (barras, líneas, etc)
# Ejemplo: gráfico de ventas, gráfico de temperatura

import matplotlib.pyplot as plt

# Datos para gráfico
meses = ['Enero', 'Febrero', 'Marzo', 'Abril']
ventas = [100, 150, 120, 200]

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(meses, ventas, marker='o', color='blue', linewidth=2)
plt.title('Ventas por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
plt.grid(True)
# plt.show()  # Descomenta para ver el gráfico
print("Gráfico creado (descomentar plt.show() para ver)")

print("\n" + "="*50 + "\n")

# 4. SEABORN (sns) - Para GRÁFICOS BONITOS
# ==========================================
# ¿Cuándo usar? Cuando quieres gráficos más bonitos que matplotlib
# Es como un "maquillaje" para gráficos

import seaborn as sns

# Hacer que los gráficos se vean más bonitos
sns.set_style("darkgrid")

# Los datos del gráfico anterior, pero más bonito
plt.figure(figsize=(10, 6))
sns.lineplot(x=meses, y=ventas, marker='o', linewidth=2, markersize=8)
plt.title('Ventas por Mes (con Seaborn)')
plt.xlabel('Mes')
plt.ylabel('Ventas ($)')
# plt.show()  # Descomenta para ver
print("Gráfico bonito creado")

print("\n" + "="*50 + "\n")

# 5. TENSORFLOW (tf) - Para INTELIGENCIA ARTIFICIAL
# ==================================================
# ¿Cuándo usar? Cuando quieres que la máquina "aprenda" de datos
# Ejemplo: reconocer imágenes, predecir precios, chatbots

# import tensorflow as tf  # Descomentar si lo instalas

# Nota: TensorFlow es complejo, por ahora no lo usamos
print("TensorFlow: Para IA avanzada (aprenderás después)")

print("\n" + "="*50 + "\n")

# RESUMEN VISUAL - CUÁNDO USAR CADA UNA
# =======================================
print("""
┌─────────────────────────────────────────────────────────────┐
│ LIBRERÍA      │ PARA QUÉ              │ ALIAS USADO        │
├─────────────────────────────────────────────────────────────┤
│ NumPy         │ Números y cálculos    │ import numpy as np │
│ Pandas        │ Tablas (como Excel)   │ import pandas as pd│
│ Matplotlib    │ Gráficos básicos      │ import matplotlib..│
│ Seaborn       │ Gráficos bonitos      │ import seaborn as s│
│ TensorFlow    │ Inteligencia Artific. │ import tensorflow.. │
└─────────────────────────────────────────────────────────────┘

REGLA DE ORO:
1. ¿Trabajas con NÚMEROS? → NumPy
2. ¿Trabajas con TABLAS/DATOS? → Pandas
3. ¿Quieres VISUALIZAR datos? → Matplotlib
4. ¿Quieres gráficos BONITOS? → Seaborn
5. ¿Haces IA/Machine Learning? → TensorFlow
""")
