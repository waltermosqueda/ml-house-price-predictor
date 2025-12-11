# ============================================
# TENSORFLOW - GUÍA RÁPIDA Y DEFINITIVA
# ============================================

# ¿QUÉ ES TENSORFLOW?
# ====================
# Es una librería que permite que las máquinas "aprendan" de datos
# Sin TensorFlow: Tú escribes reglas. Máquina sigue órdenes.
# Con TensorFlow: Máquina descubre las reglas por sí sola.

# ANALOGÍA PARA RECORDAR:
# ======================
# Imagina que quieres enseñar a un niño a reconocer gatos vs perros
#
# SIN TensorFlow (tradición):
# - Tú dices: "Si tiene orejas puntiudas = gato"
# - Tú dices: "Si mide menos de 50cm = gato"
# - Tú dices: "Si hace miau = gato"
# - Problema: ¿Y si un gato no hace miau? Falla.
#
# CON TensorFlow (aprendizaje):
# - Le muestras 10,000 fotos de gatos y perros etiquetadas
# - La máquina DESCUBRE por sí sola qué hace que sea gato o perro
# - Resultado: Reconoce gatos con 95% de precisión

print("="*60)
print("TENSORFLOW - 3 CONCEPTOS FUNDAMENTALES")
print("="*60)

# CONCEPTO 1: NEURONA ARTIFICIAL
# ================================
# Una neurona artificial es como un pequeño "cerebro" que recibe números
# y produce un número de salida

# Ejemplo simple (SIN TensorFlow):
def neurona_simple(entrada1, entrada2):
    # La neurona tiene "pesos" (importancia de cada entrada)
    peso1 = 0.5
    peso2 = 0.3
    
    # Multiplica entrada por peso y suma
    resultado = (entrada1 * peso1) + (entrada2 * peso2)
    return resultado

entrada_a = 10
entrada_b = 20
salida = neurona_simple(entrada_a, entrada_b)
print(f"\nNeurona simple:")
print(f"  Entrada 1: {entrada_a}")
print(f"  Entrada 2: {entrada_b}")
print(f"  Salida: {salida}")

# CONCEPTO 2: RED NEURONAL
# ==========================
# Una red neuronal = muchas neuronas conectadas
# Capa 1 (Entrada) → Capa 2 (Procesamiento) → Capa 3 (Salida)

# Ejemplo visual:
print("\n" + "="*60)
print("RED NEURONAL SIMPLE")
print("="*60)

estructura_red = """
CAPAS:
┌─────────────┐        ┌─────────────┐        ┌─────────────┐
│  ENTRADA    │        │ PROCESAMIENTO│       │   SALIDA    │
│  (Datos)    │───────→│  (Neuronas)  │─────→│  (Resultado)│
│             │        │              │       │             │
│ Edad: 25    │        │  Neurona 1   │       │ Predicción: │
│ Salary: 100K│─┐      │  Neurona 2   │       │  Aprobado   │
│ Historial: 8│─┼─────→│  Neurona 3   │────→ │  Crédito    │
└─────────────┘ │      └─────────────┘       └─────────────┘
                │
                └─ Los pesos se ajustan durante el aprendizaje
"""
print(estructura_red)

# CONCEPTO 3: APRENDIZAJE (Training)
# ====================================
# La máquina aprende ajustando los "pesos" de las neuronas
# hasta minimizar errores

print("\n" + "="*60)
print("PROCESO DE APRENDIZAJE")
print("="*60)

proceso = """
PASO 1: INICIO (Pesos aleatorios)
  Peso 1 = 0.2, Peso 2 = 0.8
  → Predicción: 75% exactitud (MALA)

PASO 2: AJUSTE (TensorFlow modifica pesos)
  Peso 1 = 0.4, Peso 2 = 0.6
  → Predicción: 82% exactitud (MEJOR)

PASO 3: MÁS AJUSTES
  Peso 1 = 0.5, Peso 2 = 0.5
  → Predicción: 95% exactitud (EXCELENTE)

PASO 4: MODELO ENTRENADO
  ¡La máquina aprendió!
"""
print(proceso)

# AHORA CON TENSORFLOW REAL
# ==========================
print("\n" + "="*60)
print("TENSORFLOW - CÓDIGO REAL")
print("="*60)

import tensorflow as tf
import numpy as np

print("\n✓ TensorFlow importado correctamente")

# EJEMPLO 1: PREDECIR PRECIOS DE CASAS
# ======================================
print("\n" + "-"*60)
print("EJEMPLO 1: Predecir precio de casa por tamaño")
print("-"*60)

# Datos de entrenamiento (tamaño en m², precio en miles)
tamaños = np.array([50, 100, 150, 200, 250], dtype=float)
precios = np.array([30, 60, 90, 120, 150], dtype=float)

# Crear modelo (red neuronal simple)
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilar el modelo
modelo.compile(optimizer='sgd', loss='mean_squared_error')

# Entrenar (aprender la relación: tamaño → precio)
print("\nEntrenando modelo...")
modelo.fit(tamaños, precios, epochs=100, verbose=0)
print("✓ Modelo entrenado")

# Predicción: ¿Cuánto cuesta una casa de 300 m²?
casa_nueva = np.array([300])
precio_predicho = modelo.predict(casa_nueva, verbose=0)
print(f"\nPredicción:")
print(f"  Casa de 300 m² → Precio predicho: ${precio_predicho[0][0]:.0f}k")

# EJEMPLO 2: CLASIFICACIÓN (Categorizar datos)
# ==============================================
print("\n" + "-"*60)
print("EJEMPLO 2: Clasificar flores (Iris)")
print("-"*60)

# Datos simplificados (imagina flores con 4 características)
# Características: largo_sepalo, ancho_sepalo, largo_petalo, ancho_petalo
# Categoría: 0=Iris Setosa, 1=Iris Versicolor, 2=Iris Virginica

datos_flores = np.array([
    [5.1, 3.5, 1.4, 0.2],  # Setosa
    [7.0, 3.2, 4.7, 1.4],  # Versicolor
    [6.3, 3.3, 6.0, 2.5],  # Virginica
])

categorias = np.array([0, 1, 2])  # Etiquetas

# Crear modelo clasificador
modelo_flores = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=[4]),
    tf.keras.layers.Dense(3, activation='softmax')
])

modelo_flores.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Entrenar
print("\nEntrenando modelo de clasificación...")
modelo_flores.fit(datos_flores, categorias, epochs=50, verbose=0)
print("✓ Modelo entrenado")

# Predicción: ¿Qué tipo es esta flor?
flor_nueva = np.array([[6.0, 3.0, 4.8, 1.5]])
prediccion = modelo_flores.predict(flor_nueva, verbose=0)
tipo_predicho = np.argmax(prediccion[0])
tipos = ['Setosa', 'Versicolor', 'Virginica']
print(f"\nPredicción:")
print(f"  Flor nueva → Tipo: {tipos[tipo_predicho]}")

# RESUMEN - LO QUE DEBES RECORDAR
# ==================================
print("\n" + "="*60)
print("RESUMEN - LO ESENCIAL DE TENSORFLOW")
print("="*60)

resumen = """
1. ¿QUÉ ES?
   → Librería para que máquinas aprendan de datos
   
2. ¿CÓMO FUNCIONA?
   → Tiene redes de neuronas que aprenden ajustando "pesos"
   
3. ¿PASOS PARA USAR?
   Paso 1: Preparar datos (entrada, etiqueta)
   Paso 2: Crear modelo (arquitectura de neuronas)
   Paso 3: Compilar (definir cómo aprende)
   Paso 4: Entrenar (modelo aprende del data)
   Paso 5: Predecir (usar modelo en datos nuevos)
   
4. CASOS DE USO REALES:
   ✓ Reconocer imágenes (gatos vs perros)
   ✓ Predecir precios (casas, acciones)
   ✓ Clasificar emails (spam vs no spam)
   ✓ Chatbots inteligentes (IA conversacional)
   ✓ Conducción autónoma (reconocer señales)
   
5. VENTAJA vs CÓDIGO NORMAL:
   → No escribes todas las reglas
   → La máquina descubre patrones automáticamente
   → Funciona con datos complejos (imágenes, texto, sonido)

6. MNEMOTECNIA PARA RECORDAR:
   TENSORFLOW = FLUJO de aprendizaje a través de TENSORES
   (Tensor = Array multidimensional de números)
"""

print(resumen)

# BONUS: CONCEPTOS AVANZADOS (Para después)
# ===========================================
print("\n" + "="*60)
print("CONCEPTOS PARA EL FUTURO")
print("="*60)

conceptos_futuro = """
• CNN (Convolutional Neural Network): Para reconocer imágenes
• RNN (Recurrent Neural Network): Para procesar texto/series temporales
• LSTM (Long Short-Term Memory): Para memoria a largo plazo
• Transfer Learning: Usar modelos pre-entrenados
• Fine-tuning: Adaptar modelos para tu caso específico

Por ahora, enfócate en lo básico que aprendiste arriba.
"""

print(conceptos_futuro)

print("\n✓ Tutorial completado. Ahora entiendes TensorFlow")
print("="*60)
