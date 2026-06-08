# --- Solución Ejercicio de Práctica: Sistema de Camping ---

# 1. Ingreso de datos (Input)
dias = int(input("Ingrese cantidad de días: "))
tramo = input("Ingrese su tramo (A, B, C o D): ").upper() # .upper() para evitar problemas con minúsculas

# 2. Valores base
precio_camping_por_noche = 15000
seguro_base = 5000

# Calcular valores brutos iniciales (por persona)
valor_camping_bruto = precio_camping_por_noche * dias
valor_seguro_bruto = seguro_base

# 3. Determinación del descuento para el Camping
descuento_camping = 0.0

if dias <= 5:
    if tramo == "A" or tramo == "B":
        descuento_camping = 0.10
    elif tramo == "C" or tramo == "D":
        descuento_camping = 0.05
elif 6 <= dias <= 12:
    if tramo == "A" or tramo == "B":
        descuento_camping = 0.20
    elif tramo == "C" or tramo == "D":
        descuento_camping = 0.15
else:
    # Si es mayor a 12 días
    descuento_camping = 0.0

# 4. Determinación del descuento para el Seguro
descuento_seguro = 0.0

if tramo == "A" or tramo == "B":
    descuento_seguro = descuento_seguro + 0.15 # 15% inicial
    if dias >= 10:
        descuento_seguro = descuento_seguro + 0.05 # 5% adicional

# 5. Cálculos finales (Operaciones)
valor_camping_final = valor_camping_bruto * (1 - descuento_camping)
valor_seguro_final = valor_seguro_bruto * (1 - descuento_seguro)

# 6. Mostrar resultados (Output)
# Se usa int() para mostrar los valores como enteros, tal como en los ejemplos
print(f"El valor del camping es: {int(valor_camping_final)}")
print(f"El valor del seguro es: {int(valor_seguro_final)}")