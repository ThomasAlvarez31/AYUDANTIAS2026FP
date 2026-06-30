servidores = {
    'SRV001': ['Produccion-Web',   'ubuntu',  'DC-Norte',   'H',  True,  'Chile'],
    'SRV002': ['Base-Datos-QA',    'debian',  'DC-Sur',     'M',  False, 'Argentina'],
    'SRV003': ['Backup-Core',      'redhat',  'DC-Este',    'H',  False, 'Chile'],
    'SRV004': ['Testing-Apps',     'ubuntu',  'DC-Norte',   'L',  True,  'EEUU'],
    'SRV005': ['File-Server',      'debian',  'DC-Sur',     'L',  False, 'Chile'],
    'SRV006': ['Gateway-Seguro',   'alpine',  'DC-Oeste',   'H',  True,  'Brasil'],
}

metricas = {
    'SRV001': [12500,  8],   # [Costo Mantenimiento, Alertas Activas]
    'SRV002': [15000,  0],   
    'SRV003': [8500,   3],   
    'SRV004': [4500,   1],   
    'SRV005': [3500,   12],  
    'SRV006': [9500,   0],   
}
def total_alertas_sistema(so_buscado):
    total_alertas = 0
    buscado = so_buscado.strip().lower()
    encontrado = False
    for id_srv in servidores:
        if servidores[id_srv][1].lower() == buscado:
            encontrado= True
            total_alertas += metricas[id_srv][1]
    if encontrado:
        print(f"El total de alertas activas para el SO es: {total_alertas}")
    else:
        print(f"ERROR no se encontraron servidores con el sistema operativo {so_buscado}")

def buscar_rango_costo(c_min, c_max):
    resultado = []
    for id_srv, datos_met in metricas.items():
        costo = datos_met[0]
        alertas = datos_met[1]

        if c_min <= costo <= c_max and alertas >= 0:
            nombre_srv = servidores[id_srv][0]
            resultado.append(f"{nombre_srv}--{id_srv}")

    if resultado:
        resultado.sort()
        print(f"los servidores encontrados son {resultado}")
    else:
        print("No hay servidores que cumplan con el rango")

def actualizar_costo(id_srv, nuevo_costo):
    id_upper = id_srv.strip().upper()
    if id_upper in metricas:
        metricas[id_upper][0] = nuevo_costo
        return True
    return False
def validar_texto(texto):
    return bool(texto and texto.strip())
def validar_criticidad(crit):
    return crit.strip().upper() in ['L', 'M', 'H']
def validar_costo(costo):
    return costo >0
def validar_virtual(opcion):
    return opcion.strip().lower() in ['s', 'n']

def registrar_servidor(id_srv, nom, so, dc, crit, pais, virt, costo, alertas):
    id_upper = id_srv.strip().upper()
    if id_upper in servidores or id_upper in metricas:
        return False
    virt_bool = True if virt.lower() == 's' else False
    servidores[id_upper] = [nom.strip(), so.strip().lower(), dc.strip(), crit.strip().upper(), virt_bool, pais.strip()]
    metricas[id_upper] = [costo, alertas]
    return True
def dar_de_baja_servidor(id_srv):
    id_upper = id_srv.strip().upper()
    if id_upper in servidores:
        del servidores[id_upper]
        del metricas[id_upper]
        return True
    return False
def menu_principal():
    while True:
        print("\n========== SYSMON CENTRAL MENU ==========")
        print("1. Total alertas por Sistema Operativo")
        print("2. Buscar servidores por rango de costo")
        print("3. Actualizar costo de mantenimiento")
        print("4. Registrar nuevo servidor")
        print("5. Dar de baja servidor (Eliminar)")
        print("6. Salir")
        print("=========================================")
        
        opcion = input("Ingrese opción: ").strip()

        if opcion == '1':
            so = input("Ingrese sistema operativo a consultar: ")
            total_alertas_sistema(so)
        elif opcion == '2':
            try:
                c_min = int(input("Ingrese el costo minimo de mantenimiento: "))
                c_max = int(input("Ingrese el costo maximo de mantenimiento: "))
                if c_min < 0 or c_max < 0:
                    print("Error los costos deben ser positivos")
                else:
                    buscar_rango_costo(c_min, c_max)
            except:
                print("Debe ingresar valores enteros")
        if opcion == '3':
            while True:
                id_srv = input("Ingrese el ID: ")
                try:
                    n_costo = int(input("Ingrese nuevo costo: "))
                    if validar_costo(n_costo):
                        if actualizar_costo(id_srv, n_costo):
                            print("El costo fue actualizado con exito")
                        else:
                            print("El codigo no existe")
                except:
                    print("Ingrese un numero valido")
                repetir = input("desea actualizar otro costo?(s/n) ").strip().lower()
                if repetir != 's':
                    break

        elif opcion == '4':
            print("\n--- Formulario de Alta de Servidor ---")
            id_srv = input("Ingrese ID del servidor: ")
            if id_srv.strip().upper() in servidores:
                print("[Error] El código ya existe en la infraestructura.")
                continue
                
            nom = input("Ingrese nombre: ")
            if not validar_texto(nom): print("Nombre inválido."); continue
                
            so = input("Ingrese SO: ")
            if not validar_texto(so): print("SO inválido."); continue
                
            dc = input("Ingrese Data Center: ")
            if not validar_texto(dc): print("Data Center inválido."); continue
                
            crit = input("Ingrese criticidad (L/M/H): ")
            if not validar_criticidad(crit): print("Criticidad inválida."); continue
                
            virt = input ("¿Es máquina virtual? (s/n): ")
            if not validar_virtual(virt): print("Opción inválida."); continue
                
            pais = input("Ingrese país: ")
            if not validar_texto(pais): print("País inválido."); continue
                
            try:
                costo = int(input("Ingrese costo: "))
                if not validar_costo(costo): print("Costo debe ser > 0."); continue
                    
                alerta = int(input("Ingrese alertas iniciales: "))
                if not validar_criticidad(alerta): print("Alertas deben ser >= 0."); continue
            except ValueError:
                print("[Error] Costo y alertas deben ser números enteros."); continue
                
            if registrar_servidor(id_srv, nom, so, dc, crit, virt, pais, costo, alerta):
                print("Servidor registrado de forma exitosa!")
            else:
                print("[Error] No se pudo completar el registro.")

        elif opcion == '5':
            id_srv = input("Ingrese el id del servidor a dar de baja: ")
            if dar_de_baja_servidor(id_srv):
                print("El servidor se elimino")
            else:
                print("El servidor no existe")
        elif opcion == '6':
            print("Programa finalizado")
            break
        else:
            print("Opcion invalida")

menu_principal()