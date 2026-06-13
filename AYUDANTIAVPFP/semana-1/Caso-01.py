inventario_minimarket = []

# 1. Función limpia: Recibe datos ya validados y solo construye el registro
def crear_producto(nombre, precio, stock, categoria):
    producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "categoria": categoria
    }
    return producto

# 2. Función de búsqueda (Patrón posición o -1)
def buscar_producto(inventario, nombre_buscado):
    for i in range(len(inventario)):
        if inventario[i]["nombre"].lower() == nombre_buscado.lower():
            return i 
    return -1

# 3. Reabastecer (Mutabilidad y Reutilización)
def reabastecer_producto(inventario, nombre_buscado, cantidad):
    posicion = buscar_producto(inventario, nombre_buscado)
    if posicion != -1:
        inventario[posicion]["stock"] += cantidad
        print(f"¡Stock actualizado! Nuevo stock: {inventario[posicion]['stock']}")
    else:
        print("Producto no encontrado.")

# 4. Mostrar Inventario de forma bonita (Concepto 8 del torpedo)
def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("\nEl inventario está vacío.")
    else:
        print("\n=== LISTA DE PRODUCTOS ===")
        for prod in inventario:
            print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']} | Stock: {prod['stock']} unidades | Cat: {prod['categoria']}")

# --- MENÚ PRINCIPAL ---
while True:
    print("\n--- MINIMARKET DON TITO ---")
    print("1. Registrar nuevo producto")
    print("2. Reabastecer stock")
    print("3. Ver inventario completo") # ¡Agregada!
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("\n--- REGISTRAR PRODUCTO ---")
        
        # Validación de Nombre
        while True:
            nom = input("Nombre del producto: ").strip()
            if nom != "":
                break
            print("Error: El nombre no puede estar vacío.")
            
        # Validación de Precio
        while True:
            pre_str = input("Precio: ")
            if pre_str.isdigit() and int(pre_str) > 0:
                pre = int(pre_str)
                break
            print("Error: El precio debe ser un número mayor a 0.")
            
        # Validación de Stock
        while True:
            stk_str = input("Stock inicial: ")
            if stk_str.isdigit() and int(stk_str) > 0:
                stk = int(stk_str)
                break
            print("Error: El stock debe ser un número mayor a 0.")
            
        cat = input("Categoría: ")
        
        # Creación directa y segura
        nuevo = crear_producto(nom, pre, stk, cat)
        inventario_minimarket.append(nuevo)
        print(f"\n✅ ¡{nom} agregado con éxito al inventario!")
            
    elif opcion == "2":
        print("\n--- REABASTECER STOCK ---")
        nom = input("¿Qué producto desea reabastecer?: ")
        cant_str = input("¿Cuántas unidades llegan?: ")
        if cant_str.isdigit() and int(cant_str) > 0:
            reabastecer_producto(inventario_minimarket, nom, int(cant_str))
        else:
            print("Cantidad inválida.")
            
    elif opcion == "3":
        # Llamamos a la función para ver el stock de forma ordenada
        mostrar_inventario(inventario_minimarket)
            
    elif opcion == "4":
        print("¡Adiós Don Tito!")
        break
    else:
        print("Opción no válida. Intente otra vez.")