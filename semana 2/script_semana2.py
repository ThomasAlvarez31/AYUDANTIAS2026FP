
def calcular_tasa(ingresos, edad):
    """
    Calcula la tasa de interés final aplicando las reglas de negocio.
    """
    tasa_base = 0.015  # 1.5%
    if ingresos > 1000000:
        if edad <= 30:
            tasa_final = tasa_base - 0.002  # Queda en 1.3%
        else:
            tasa_final = tasa_base - 0.004  # Queda en 1.1%
    else:
        tasa_final = tasa_base  # Se mantiene igual
    return tasa_final
# 2. Control del Programa Principal (Menú con while)
continuar = True
print("=== BIENVENIDO AL SISTEMA DE CRÉDITOS ===")
while continuar:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Calcular Simulación de Crédito")
    print("2. Salir del Programa")
    opcion = input("Seleccione una opción (1 o 2): ")
    if opcion == "1":
        print("\n--- NUEVA SIMULACIÓN ---")
        # Validación del monto solicitado (Bucle de validación)
        monto = int(input("Ingrese monto a solicitar ($500.000 a $5.000.000): "))
        while monto < 500000 or monto > 5000000:
            print("ERROR: Monto fuera de rango permitido.")
            monto = int(input("Por favor, ingrese un monto válido: "))
        # Validación de las cuotas
        cuotas = int(input("Ingrese cantidad de cuotas (12, 24 o 36): "))
        while cuotas != 12 and cuotas != 24 and cuotas != 36:
            print("ERROR: Cantidad de cuotas no permitida.")
            cuotas = int(input("Por favor, ingrese 12, 24 o 36: "))
        # Ingreso de datos del perfil del cliente
        ingresos = int(input("Ingrese sus ingresos mensuales bruto: $"))
        edad = int(input("Ingrese su edad: "))
        # 3. Uso de la función
        tasa_aplicada = calcular_tasa(ingresos, edad)
        # 4. Operaciones matemáticas
        valor_cuota = (monto * (1 + tasa_aplicada)) / cuotas
        # 5. Output de resultados
        print("\n>>> RESULTADOS DE LA SIMULACIÓN <<<")
        print(f"Monto aprobado: ${monto:,}")
        print(f"Tasa de interés aplicada: {tasa_aplicada * 100:.1f}%")
        # Se usa int() para redondear a entero el valor monetario final
        print(f"El valor de su cuota mensual es: ${int(valor_cuota):,}")
    elif opcion == "2":
        print("\nGracias por utilizar el simulador. ¡Hasta pronto!")
        continuar = False # Rompe el bucle de menú de forma limpia
    else:
        print("Opción inválida. Intente nuevamente.")