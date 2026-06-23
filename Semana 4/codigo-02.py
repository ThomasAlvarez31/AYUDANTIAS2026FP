def clasificar_peligrosidad(impacto):
    if 1<= impacto <= 3:
        return "bajo"
    elif 4<= impacto <= 6:
        return "medio"
    elif 7<= impacto <= 8:
        return "alto"
    elif 9<= impacto <= 10:
        return "critico"
    else:
        raise ValueError("El impacto debe estar estrictamente entre 1 y 10")
    
def registrar_incidente(historial, id_actual, servidor, tipo, impacto_str):
    try:
        impacto = int(impacto_str)
        peligrosidad = clasificar_peligrosidad(impacto)

        nuevo_incidente= {
            "id": id_actual,
            "servidor": servidor,
            "tipo":tipo,
            "impacto": impacto,
            "peligrosidad": peligrosidad
        }
        historial.append(nuevo_incidente)
        print(f"\n[EXITO]Incidente {id_actual} registrado como {peligrosidad}")
        return True
    except ValueError as error:
        print(f"\n [ERROR] DE VALIDACION no se puede registrar: {error}")
        return False
    
def consultar_incidente_por_indice(historial):
    print("Consultar incidente por posicion")
    pos_str = input("ingrese el indice del reporte a consultar: ")
    try:
        pos = int(pos_str)
        incidente = historial[pos]
        print(f"\n[ID {incidente['id']}] Servidor: {incidente['servidor']} | Tipo: {incidente['tipo']} | Peligrosidad: {incidente['peligrosidad']}")
    except ValueError:
        print("Error debe ingresar un numero entero valido para el indice")
    except IndexError:
        print(f"posicion invalida, el rango del historial es de 0 a {len(historial) - 1}")

def simular_analisis_avanzado(historial):
    print("procesamiento de seguridad(simulacion)")
    pos_str = input("Seleccione el inidce del incidente para analizar")

    try:
        pos = int(pos_str)

        incidente = historial[pos]
        if incidente['peligrosidad'] == "bajo":
            calculo_raro = 100/0
        print("analisis completado con exito para el incidente")
    except Exception as e:
        print(f"Ocurrio un error inesperado al procesar: {type(e).__name__} -> {e}")
def menu():
    incidentes_log = []
    contador_id = 1
    
    while True:
        print("\n=== CONSOLA SOC - CYBERSHIELD ===")
        print("1. Reportar nuevo incidente (Clasificación)")
        print("2. Consultar incidente por índice")
        print("3. Ejecutar análisis avanzado (Test de Errores)")
        print("4. Ver todos los incidentes")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            print("\nregistro de nuevo incidente")
            servidor = input("Nombre del Servidor afectado (ej. Producción_01): ").strip()
            tipo = input("Tipo de ataque (ej. Ransomware / DDoS): ").strip()
            impacto_raw = input("Nivel de impacto (1 al 10): ").strip()
            if registrar_incidente(incidentes_log, contador_id, servidor, tipo, impacto_raw):
                contador_id +=1
        elif opcion == "2":
            if len(incidentes_log) == 0:
                print("Nohay incidentes registrados")
            else:
                consultar_incidente_por_indice(incidentes_log)
        elif opcion == "3":
            if len(incidentes_log) == 0:
                print("No hay datos para consultar")
            else:
                simular_analisis_avanzado(incidentes_log)
        elif opcion == "4":
            if not incidentes_log:
                print("Historial limpio no hay amenazas")
            else:
                for inc in incidentes_log:
                    print(f"ID: {inc['id']} | Servidor: {inc['servidor']} | Tipo: {inc['tipo']} | Impacto: {inc['impacto']}/10 -> [{inc['peligrosidad']}]")

        elif opcion == "5":
            print("Hasta luego")
            break
        else:
            print("Opcion no valida, intente nuevamente")
menu()