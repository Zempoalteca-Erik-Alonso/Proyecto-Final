esta interfaz tendra que llevar el registro de asistencias asi como tambien el control de las vacaciones o "dias economicos"
se define como dirigida para el sector salud, especificamente para un hospital del cual se llevara el control de asistencias
para crear esta interfaz se usara python, por lo cual es importante saber que herramientas se pueden utilizar dentro de este lenguaje de programacion para poder ejecutarlo de una buena manera 
las herramientas que se usaran serán:

1. Tkinter (para la interfaz gráfica)
Viene incluido con Python.
Perfecta para aplicaciones de escritorio pequeñas o medianas.
Fácil de implementar botones, formularios, calendarios básicos y tablas simples.

2. SQLite (para almacenamiento local)
También viene integrado en Python (sqlite3).
Ideal para guardar usuarios, asistencias, solicitudes, etc.
Muy estable y confiable para apps locales.

se hará que estas dos herramientas/librerias traben juntas de la siguiente manera:
- Tkinter muestra la interfaz: formularios de registro, botones de entrada/salida, menús para solicitar vacaciones, etc.
- SQLite guarda los datos: registros de asistencia, usuarios, solicitudes, permisos.
- Python conecta ambos: cuando un usuario marca asistencia, se registra en SQLite; cuando solicita vacaciones, se guarda como un nuevo registro.
asi, se usara tkinter principalmente para loa creacion y funcion de botones y SQLite para el guardado de los datos, Python será el lenguaje que conectara ambas herramientas/librerias para su trabajo en conjunto


