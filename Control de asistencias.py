def registrar_empleado():
    print("=== REGISTRO DE EMPLEADOS ===")
    id_empleado = input("ID del empleado: ")
    nombre = input("Nombre completo: ")
    rol = input("Área o rol (por ejemplo: Médico, Enfermero, etc.): ")
    linea = f"{id_empleado},{nombre},{rol}\n"
    with open("empleados.txt", "a", encoding="utf-8") as archivo:
        archivo.write(linea)
    print("Empleado registrado con éxito.\n")
def main():
    while True:
        registrar_empleado()
        otra = input("¿Deseas registrar otro empleado? (s/n): ")
        if otra.lower() != 's':
            print("Saliendo del registro.")
            break
if __name__ == "__main__":
    main()