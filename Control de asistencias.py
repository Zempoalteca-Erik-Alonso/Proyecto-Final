from datetime import datetime
def registrar_empleado():
    print("=== REGISTRO DE EMPLEADOS ===")
    id_empleado = input("ID del empleado: ")
    nombre = input("Nombre completo: ")
    rol = input("Área o rol (por ejemplo: Médico, Enfermero, etc.): ")
    linea = f"{id_empleado},{nombre},{rol}\n"
    with open("empleados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    print("Empleado registrado con éxito.\n")
def validar_empleado(id_empleado):
    try:
        with open("empleados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith(id_empleado + ","):
                    return True
    except FileNotFoundError:
        print("Error.")
    return False
def registrar_asistencia():
    print("REGISTRO DE ASISTENCIAS")
    id_empleado = input("ID del empleado: ")
    if not validar_empleado(id_empleado):
        print("ID no encontrado..\n")
        return
    tipo = input("entrada o salida? (E/S): ").strip().upper()
    if tipo not in ["E", "S"]:
        print("Error")
        return
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M:%S")
    linea = f"{id_empleado},{tipo},{fecha},{hora}\n"
    with open("asistencias.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    print("asistencia registrada.\n")
def empleado_y_asistencias():
    print("CHECAR EMPLEADO Y ASISTENCIAS")
    id_empleado = input("Ingrese el ID del empleado: ")
    try:
        with open("empleados.txt", "r", encoding="utf-8") as emp:
            encontrado = False
            for linea in emp:
                if linea.startswith(id_empleado + ","):
                    print(f"empleado: {linea.strip()}")
                    encontrado = True
                    break
            if not encontrado:
                print("empleado no encontrado")
                return
    except FileNotFoundError:
        print("error:")
        return
    print("\nhistorial de sus asistencias:")
    try:
        with open("asistencias.txt", "r", encoding="utf-8") as asist:
            contador = 0
            for linea in asist:
                if linea.startswith(id_empleado + ","):
                    print(f" - {linea.strip()}")
                    contador += 1
            if contador == 0:
                print("no hay asistencias")
    except FileNotFoundError:
        print("no se ha registrado asistencia todavia")
def main():
    while True:
        print("MENU PRINCIPAL")
        print("1. registrar a un empleado")
        print("2. asistencia")
        print("3. checar empleado y asistencias")
        print("4. Salir")
        opcion = input("elige una opción (1/2/3/4): ")
        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            registrar_asistencia()
        elif opcion == "3":
             empleado_y_asistencias()
        elif opcion == "4":
            print("saliendo.")
            break
        else:
            print("error\n")
if __name__ == "__main__":
    main()
