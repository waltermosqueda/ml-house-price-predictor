"""
Script para hacer predicciones con el modelo entrenado
Uso: python predict.py
"""

import pickle
import pandas as pd
import numpy as np

print("="*60)
print("PREDICTOR DE PRECIOS DE CASAS")
print("="*60)

# Cargar el modelo y escalador
try:
    with open('models/modelo_precios.pkl', 'rb') as f:
        modelo = pickle.load(f)
    
    with open('models/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    
    print("\n✓ Modelo cargado correctamente")
except FileNotFoundError:
    print("❌ Error: Primero debes entrenar el modelo")
    print("Ejecuta: python train.py")
    exit()

# Función para hacer predicción
def predecir_precio(metros_cuadrados, cuartos, edad_casa, distancia_centro):
    """
    Predice el precio de una casa
    
    Parámetros:
    - metros_cuadrados: Tamaño de la casa en m²
    - cuartos: Número de cuartos
    - edad_casa: Edad de la casa en años
    - distancia_centro: Distancia al centro en km
    """
    
    # Crear DataFrame con los datos
    datos = pd.DataFrame({
        'metros_cuadrados': [metros_cuadrados],
        'cuartos': [cuartos],
        'edad_casa': [edad_casa],
        'distancia_centro': [distancia_centro]
    })
    
    # Normalizar datos
    datos_escalados = scaler.transform(datos)
    
    # Hacer predicción
    precio_predicho = modelo.predict(datos_escalados)[0]
    
    return precio_predicho

# MENÚ INTERACTIVO
# ================
print("\n" + "-"*60)
print("CÓMO USAR:")
print("-"*60)
print("Ingresa las características de la casa y predice su precio")
print("(Escribe 'salir' para terminar)")
print()

while True:
    try:
        print("\n" + "="*60)
        
        # Pedir datos al usuario
        entrada = input("¿Metros cuadrados? (o 'salir'): ").strip().lower()
        if entrada == "salir":
            print("\n¡Gracias por usar el predictor!")
            break
        
        metros = float(entrada)
        cuartos = int(input("¿Número de cuartos? "))
        edad = int(input("¿Edad de la casa (años)? "))
        distancia = float(input("¿Distancia al centro (km)? "))
        
        # Validar datos
        if metros <= 0 or cuartos <= 0 or edad < 0 or distancia < 0:
            print("❌ Error: Ingresa valores válidos (positivos)")
            continue
        
        # Hacer predicción
        precio = predecir_precio(metros, cuartos, edad, distancia)
        
        # Mostrar resultado
        print("\n" + "="*60)
        print("PREDICCIÓN DE PRECIO")
        print("="*60)
        print(f"\nCaracterísticas ingresadas:")
        print(f"  • Metros cuadrados: {metros} m²")
        print(f"  • Cuartos: {cuartos}")
        print(f"  • Edad de la casa: {edad} años")
        print(f"  • Distancia al centro: {distancia} km")
        print(f"\n💰 PRECIO PREDICHO: ${precio:,.2f}")
        print("\n" + "="*60)
        
    except ValueError:
        print("❌ Error: Ingresa valores numéricos válidos")
    except KeyboardInterrupt:
        print("\n\n¡Gracias por usar el predictor!")
        break

# EJEMPLOS DE PREDICCIÓN
# ======================
print("\n" + "="*60)
print("EJEMPLOS DE PREDICCIÓN (sin interacción)")
print("="*60)

ejemplos = [
    {"metros": 100, "cuartos": 3, "edad": 10, "distancia": 5},
    {"metros": 200, "cuartos": 4, "edad": 5, "distancia": 2},
    {"metros": 150, "cuartos": 3, "edad": 20, "distancia": 10},
]

for i, ejemplo in enumerate(ejemplos, 1):
    precio = predecir_precio(
        ejemplo["metros"],
        ejemplo["cuartos"],
        ejemplo["edad"],
        ejemplo["distancia"]
    )
    
    print(f"\nEjemplo {i}:")
    print(f"  {ejemplo['metros']}m² | {ejemplo['cuartos']} cuartos | {ejemplo['edad']} años | {ejemplo['distancia']}km")
    print(f"  → Precio predicho: ${precio:,.2f}")

print("\n" + "="*60)
