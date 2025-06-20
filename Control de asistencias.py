import tkinter as tk
from tkinter import messagebox
from datetime import datetime
def registrar_empleado():
    id_emp = entry_id_emp.get()
    nombre = entry_nombre.get()
    rol = entry_rol.get()
    if not id_emp or not nombre or not rol:
        messagebox.showwarning("aviso", "faltan datos")
        return
    with open("empleados.txt", "a", encoding="utf-8") as f:
        f.write(f"{id_emp},{nombre},{rol}\n")
    messagebox.showinfo("Éxito", "Empleado registrado.")
    entry_id_emp.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_rol.delete(0, tk.END)
def validar_empleado(id_empleado):
    try:
        with open("empleados.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.startswith(id_empleado + ","):
                    return True
    except FileNotFoundError:
        return False
    return False
def registrar_asistencia():
    id_emp = entry_asist_id.get()
    tipo = var_asist_tipo.get()
    if not validar_empleado(id_emp):
        messagebox.showerror("Error", "El empleado no está registrado.")
        return
    if tipo not in ["E", "S"]:
        messagebox.showerror("Error", "(E) entrada (S) salida")
        return
    ahora = datetime.now()
    fecha = ahora.strftime("%Y-%m-%d")
    hora = ahora.strftime("%H:%M:%S")    
    with open("asistencias.txt", "a", encoding="utf-8") as f:
        f.write(f"{id_emp},{tipo},{fecha},{hora}\n")
    messagebox.showinfo("aviso", "asistencia registrada.")
    entry_asist_id.delete(0, tk.END)
def empleado_y_asistencias():
    id_emp = entry_consulta_id.get()
    resultado = ""
    try:
        with open("empleados.txt", "r", encoding="utf-8") as f:
            for linea in f:
                if linea.startswith(id_emp + ","):
                    resultado += "Empleado: " + linea
                    break
            else:
                resultado += "Empleado no encontrado.\n"
    except FileNotFoundError:
        resultado += "no existe el archivo\n"
    resultado +="\nasistencias:\n"
    try:
        with open("asistencias.txt", "r", encoding="utf-8") as f:
            for linea in f:
                if linea.startswith(id_emp + ","):
                    resultado += " - " + linea
    except FileNotFoundError:
        resultado+= "no hay asistencias\n"
    messagebox.showinfo("resultado", resultado)
def dia_justificado():
    id_emp = entry_just_id.get()
    tipo = var_just_tipo.get()
    fecha = entry_just_fecha.get()
    if not validar_empleado(id_emp):
        messagebox.showerror("Error", "no esta registrado")
        return
    if tipo not in ["vacaciones", "economico"]:
        messagebox.showerror("Error", "Error")
        return
    with open("justificaciones.txt", "a", encoding="utf-8") as f:
        f.write(f"{id_emp},{tipo},{fecha}\n")
    messagebox.showinfo("aviso", "dia justificado registrado.")
    entry_just_id.delete(0, tk.END)
    entry_just_fecha.delete(0, tk.END)
def anular_justificado():
    id_emp = entry_anular_id.get()
    tipo = var_anular_tipo.get()
    fecha = entry_anular_fecha.get()
    try:
        with open("justificaciones.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        messagebox.showerror("error", "no se encontro el archivo de las justificaciones")
        return
    nueva_lista = []
    encontrado = False
    for linea in lineas:
        if linea.strip() != f"{id_emp},{tipo},{fecha}":
            nueva_lista.append(linea)
        else:
            encontrado = True
    if encontrado:
        with open("justificaciones.txt", "w", encoding="utf-8") as f:
            f.writelines(nueva_lista)
        messagebox.showinfo("ventana", "justificacion eliminada.")
    else:
        messagebox.showinfo("error", "la justificacion no se encontro o no existe")
    entry_anular_id.delete(0, tk.END)
    entry_anular_fecha.delete(0, tk.END)
ventana = tk.Tk()
ventana.title("Sistema de Control de Asistencias - Hospital")
tk.Label(ventana, text="registro de empleado").grid(row=0, column=0, columnspan=2)
tk.Label(ventana, text="ID:").grid(row=1, column=0)
entry_id_emp = tk.Entry(ventana)
entry_id_emp.grid(row=1, column=1)
tk.Label(ventana, text="nombre:").grid(row=2, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=2, column=1)
tk.Label(ventana, text="rol/area:").grid(row=3, column=0)
entry_rol = tk.Entry(ventana)
entry_rol.grid(row=3, column=1)
tk.Button(ventana, text="registrar empleado", command=registrar_empleado).grid(row=4, column=0, columnspan=2)
tk.Label(ventana, text="\nRegistrar asistencia").grid(row=5, column=0, columnspan=2)
tk.Label(ventana, text="ID:").grid(row=6, column=0)
entry_asist_id = tk.Entry(ventana)
entry_asist_id.grid(row=6, column=1)
tk.Label(ventana, text="tipo (E/S):").grid(row=7, column=0)
var_asist_tipo = tk.StringVar()
tk.Entry(ventana, textvariable=var_asist_tipo).grid(row=7, column=1)
tk.Button(ventana, text="registrar asistencia", command=registrar_asistencia).grid(row=8, column=0, columnspan=2)
tk.Label(ventana, text="\nconsulta de empleado").grid(row=9, column=0, columnspan=2)
tk.Label(ventana, text="ID:").grid(row=10, column=0)
entry_consulta_id = tk.Entry(ventana)
entry_consulta_id.grid(row=10, column=1)
tk.Button(ventana, text="consultar", command=empleado_y_asistencias).grid(row=11, column=0, columnspan=2)
tk.Label(ventana, text="\njustificacion (vacaciones/dia economico)").grid(row=12, column=0, columnspan=2)
tk.Label(ventana, text="ID:").grid(row=13, column=0)
entry_just_id = tk.Entry(ventana)
entry_just_id.grid(row=13, column=1)
tk.Label(ventana, text="tipo:").grid(row=14, column=0)
var_just_tipo = tk.StringVar()
tk.Entry(ventana, textvariable=var_just_tipo).grid(row=14, column=1)
tk.Label(ventana, text="fecha (YYYY-MM-DD):").grid(row=15, column=0)
entry_just_fecha = tk.Entry(ventana)
entry_just_fecha.grid(row=15, column=1)
tk.Button(ventana, text="registrar justificacion", command=dia_justificado).grid(row=16, column=0, columnspan=2)
tk.Label(ventana, text="\nAnular día justificado").grid(row=17, column=0, columnspan=2)
tk.Label(ventana, text="ID:").grid(row=18, column=0)
entry_anular_id = tk.Entry(ventana)
entry_anular_id.grid(row=18, column=1)
tk.Label(ventana, text="Tipo:").grid(row=19, column=0)
var_anular_tipo = tk.StringVar()
tk.Entry(ventana, textvariable=var_anular_tipo).grid(row=19, column=1)
tk.Label(ventana, text="Fecha (YYYY-MM-DD):").grid(row=20, column=0)
entry_anular_fecha = tk.Entry(ventana)
entry_anular_fecha.grid(row=20, column=1)
tk.Button(ventana, text="Eliminar Justificación", command=anular_justificado).grid(row=21, column=0, columnspan=2)
ventana.mainloop()
