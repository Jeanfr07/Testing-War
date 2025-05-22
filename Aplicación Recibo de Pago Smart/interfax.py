import tkinter.simpledialog as simpledialog
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
import mysql.connector
from mysql.connector import Error
import re
from conexion import conectar as conectar_db 
image = None
photo = None
screen_width = None
screen_height = None

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Usuario de la base de datos
        password="root",  # Contraseña de la base de datos
        database="smartdb"  # Nombre de la base de datos
    )

# Cargar la imagen una vez
def cargar_imagen():
    global image, photo, screen_width, screen_height
    image = Image.open("centro.jpeg")
    image = image.resize((screen_width, screen_height))
    enhancer = ImageEnhance.Brightness(image)
    dark_image = enhancer.enhance(0.5)
    photo = ImageTk.PhotoImage(dark_image)

# Imagen de fondo a una ventana
def agregar_imagen_fondo(ventana):
    fondo_label = tk.Label(ventana, image=photo)
    fondo_label.image = photo  
    fondo_label.pack(expand=True, fill="both")
    return fondo_label

def opc_eliminar():
    opcion=eliminar_opc.get()
    if opcion == "1":
        eliminar_curso()
    else:
        messagebox.showerror("Error", "Ingrese un número del 1 al 5")
def opc_modificar():
    opcion=modificar_opc.get()
    if opcion == "1":
        insertar_Alumno() #modificar alumno
    elif opcion == "2": 
        insertar_Curso() #modificar curso
    elif opcion == "3":
        insertar_Coordinacion() #modificar coordinacion
    elif opcion == "4":
        insertar_Transaccion() #modificar correo
    elif opcion == "5":
        isnertar_recibo() #modificar telefono alumno
    elif opcion == "6":
        isnertar_recibo() #modificar telefono coordinacion
    else:
        messagebox.showerror("Error", "Ingrese un número del 1 al 6")
        
def opc_insertar():
    opcion=entrar_opc.get()
    if opcion == "1":
        insertar_Alumno() 
        menu_insertar.destroy
    elif opcion == "2": 
        insertar_Curso()
    elif opcion == "3":
        insertar_Coordinacion() 
    elif opcion == "4":
        insertar_Transaccion() 
    elif opcion == "5":
        isnertar_recibo()
    else:
        messagebox.showerror("Error", "Ingrese un número del 1 al 5")
    
def manejar_opcion():
    opcion = entry_opcion.get()
    if opcion == "1":
        menu_insertar()
    elif opcion == "2":
        menu_modificar()
    elif opcion == "3":
        menu_eliminar()
    elif opcion == "4":
        menu_consultar()
    else:
        messagebox.showerror("Error", "Ingrese un número del 1 al 4")
#eliminar curso
def eliminar_curso():
    def validar():
        codigo=codigo_entry.get().strip()
        if len(codigo) == 3:
            messagebox.showinfo("Bien",f"Se elimino el curso '{codigo}'")
            curso_eliminar.destroy
        else:
            messagebox.showerror("Error", "Ingrese un código valido")
    curso_eliminar=tk.Toplevel()
    curso_eliminar.title("Eliminar Curso")
    curso_eliminar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(curso_eliminar)
    tk.Label(
        curso_eliminar,
        text="Eliminar Curso",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")
    frame_formulario = tk.Frame(curso_eliminar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    tk.Label(
        frame_formulario,
        text="Código del Curso:",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).grid(row=0, column=0, sticky="e", pady=10, padx=10)

    codigo_entry = tk.Entry(frame_formulario, font=("Helvetica", 16), width=10)
    codigo_entry.grid(row=0, column=1, pady=10, padx=10)

    frame_botones = tk.Frame(curso_eliminar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.7, anchor="center")

    btn_eliminar = tk.Button(
        frame_botones,
        text="Eliminar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar
    )
    btn_eliminar.grid(row=0, column=0, padx=10)

    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=curso_eliminar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)
    
#modificar alumno
   

# insertar alumno
def insertar_Alumno():
    def validar_datos():
        dni = entradas["DNI"].get().strip()
        primer_nombre = entradas["Primer Nombre"].get().strip()
        segundo_nombre = entradas["Segundo Nombre"].get().strip()
        apellido_paterno = entradas["Apellido Paterno"].get().strip()
        apellido_materno = entradas["Apellido Materno"].get().strip()
        genero = entradas["Género"].get().strip()
        fecha_nacimiento = entradas["Fecha de Nacimiento"].get().strip()
        lugar_procedencia = entradas["Lugar de Procedencia"].get().strip()
        codigo_curso = entradas["Código Curso"].get().strip()
        correo = entradas["Correo"].get().strip()
        celular = entradas["Numero Celular"].get().strip()
        dni_coordinacion = entradas["DNI Coordinación"].get().strip()

        # Validación de los campos
        if not dni.isdigit() or len(dni) != 8:
            messagebox.showerror("Error", "El DNI debe contener 8 dígitos numéricos.")
            return
        if not primer_nombre.isalpha():
            messagebox.showerror("Error", "Primer nombre debe contener solo letras.")
            return
        if segundo_nombre and not segundo_nombre.isalpha():
            messagebox.showerror("Error", "Segundo nombre debe contener solo letras.")
            return
        if not apellido_paterno.isalpha():
            messagebox.showerror("Error", "Apellido paterno debe contener solo letras.")
            return
        if not apellido_materno.isalpha():
            messagebox.showerror("Error", "Apellido materno debe contener solo letras.")
            return
        if genero.upper() not in ["M", "F"]:
            messagebox.showerror("Error", "Ingrese solo F o M en el género")
            return
        if not validar_fecha(fecha_nacimiento):
            messagebox.showerror("Error", "La Fecha de Nacimiento debe tener el formato YYYY-MM-DD.")
            return
        if not lugar_procedencia:
            messagebox.showerror("Error", "El Lugar de Procedencia no puede estar vacío.")
            return
        if not correo or "@" not in correo:
            messagebox.showerror("Error", "Correo electrónico no válido.")
            return
        if not celular.isdigit() or len(celular) != 9:
            messagebox.showerror("Error", "Número de celular debe contener 9 dígitos numéricos.")
            return
        if not dni_coordinacion.isdigit() or len(dni_coordinacion) != 8:
            messagebox.showerror("Error", "DNI de la Coordinación debe contener 8 dígitos numéricos.")
            return
        if not codigo_curso or len(codigo_curso) != 3:
            messagebox.showerror("Error", "Código de curso debe tener exactamente 3 caracteres.")
            return

        # Intentar insertar el alumno usando el procedimiento
        try:
            conexion = conectar_db()
            cursor = conexion.cursor()
            cursor.callproc('InsertarAlumno', [
                dni, primer_nombre, segundo_nombre, apellido_paterno, apellido_materno, genero,
                fecha_nacimiento, lugar_procedencia, codigo_curso, correo, celular, dni_coordinacion
            ])
             conexion.commit()
            messagebox.showinfo("Éxito", "Alumno ingresado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al insertar el alumno: {e}")
            return
            finally:
    cursor.close()
    conexion.close()

    def validar_fecha(fecha):
        # Validación del formato YYYY-MM-DD
        patron = r"^\d{4}-\d{2}-\d{2}$"
        return re.match(patron, fecha) is not None

    alumno_insertar = tk.Toplevel()
    alumno_insertar.title("Menu Insertar Alumno")
    alumno_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(alumno_insertar)

    tk.Label(
        alumno_insertar,
        text="Insertar Alumno",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_formulario = tk.Frame(alumno_insertar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    campos = [
        ("DNI", "DNI"),
        ("Primer Nombre", "Primer Nombre"),
        ("Segundo Nombre", "Segundo Nombre"),
        ("Apellido Paterno", "Apellido Paterno"),
        ("Apellido Materno", "Apellido Materno"),
        ("Género", "Género"),
        ("Fecha de Nacimiento", "Fecha de Nacimiento"),
        ("Lugar de Procedencia", "Lugar de Procedencia"),
        ("Código Curso", "Código Curso"),
        ("Correo", "Correo"),
        ("Numero Celular", "Numero Celular"),
        ("DNI Coordinación", "DNI Coordinación"),
    ]

    entradas = {}
    for idx, (etiqueta, clave) in enumerate(campos):
        tk.Label(
            frame_formulario,
            text=etiqueta,
            font=("Helvetica", 16),
            fg="black",
            bg="white"
        ).grid(row=idx, column=0, sticky="e", pady=5, padx=5)

        entrada = tk.Entry(frame_formulario, font=("Helvetica", 16), width=30)
        entrada.grid(row=idx, column=1, pady=5, padx=5)
        entradas[clave] = entrada

    frame_botones = tk.Frame(alumno_insertar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.8, anchor="center")

    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar_datos
    )
    btn_guardar.grid(row=0, column=0, padx=10)

    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=alumno_insertar.destroy
    )
    btn_regresar.grid(row=0, column=1, padx=10)
        
#insertar curso
def insertar_Curso():
    def validar_datos():
        codigo = entradas["Codigo"].get().strip()
        nombre = entradas["Nombre"].get().strip()
        idioma = entradas["Idioma"].get().strip()
        precio = entradas["Precio"].get().strip()
        docente = entradas["Docente Encargado"].get().strip()
        nivel = entradas["Nivel"].get().strip()
        max_alumnos = entradas["Máximo de alumnos"].get().strip()
        if not codigo.isalnum() or len(codigo) != 3:
            messagebox.showerror("Error", "El Código debe ser alfanumérico y tener exactamente 3 caracteres.")
            return
        if not nombre or not nombre.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El Nombre debe contener solo letras.")
            return
        if not idioma or not idioma.isalpha():
            messagebox.showerror("Error", "El Idioma debe contener solo letras.")
            return
        if not precio.isdigit() or float(precio) <= 0.0:
            messagebox.showerror("Error", "El Precio debe ser un número mayor a 0.0")
            return
        if not docente or not docente.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El Docente Encargado debe contener solo letras.")
            return
        if not nivel:
            messagebox.showerror("Error", "El nivel no puede estar vacío.")
            return
        if not max_alumnos.isdigit() or int(max_alumnos) <= 0:
            messagebox.showerror("Error", "El Máximo de Alumnos debe ser un número mayor a 0.")
            return
        messagebox.showinfo("Éxito", "Datos ingresados correctos")

    curso_insertar = tk.Toplevel()
    curso_insertar.title("Insertar Curso")
    curso_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(curso_insertar)
    tk.Label(
        curso_insertar,
        text="Insertar Curso",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")
    
    frame_formulario = tk.Frame(curso_insertar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    campos = [
        ("Codigo", ""),
        ("Nombre", ""),
        ("Idioma", ""),
        ("Precio", ""),
        ("Docente Encargado", ""),
        ("Nivel", "genero"),
        ("Máximo de alumnos", ""),
    ]

    entradas = {}
    for idx, (etiqueta, clave) in enumerate(campos):
        tk.Label(
            frame_formulario,
            text=etiqueta,
            font=("Helvetica", 16),
            fg="black",
            bg="white"
        ).grid(row=idx, column=0, sticky="e", pady=5, padx=5)
        
        entrada = tk.Entry(frame_formulario, font=("Helvetica", 16), width=30)
        entrada.grid(row=idx, column=1, pady=5, padx=5)
        entradas[clave] = entrada
    frame_botones = tk.Frame(curso_insertar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.8, anchor="center")
    
    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar_datos
    )
    btn_guardar.grid(row=0, column=0, padx=10)
    
    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=curso_insertar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)
    
    
#insertar coordinacion
def insertar_Coordinacion():
    def validar_datos():
        dni = entradas["DNI"].get().strip()
        nombres = entradas["Nombres"].get().strip()
        apellidos = entradas["Apellidos"].get().strip()
        correo = entradas["Correo"].get().strip()
        if not dni.isdigit() or len(dni) != 8:
            messagebox.showerror("Error", "El DNI debe contener 8 dígitos numéricos.")
            return
        if not nombres or not nombres.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Los Nombres deben contener solo letras.")
            return
        if not apellidos or not apellidos.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Los Apellidos deben contener solo letras.")
            return
        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "El Correo debe tener un formato válido (ejemplo: correo@dominio.com).")
            return
        messagebox.showinfo("Éxito", "Datos ingresados correctamente")
    coordinacion_insertar = tk.Toplevel()
    coordinacion_insertar.title("Insertar Coordinación")
    coordinacion_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(coordinacion_insertar)
    tk.Label(
        coordinacion_insertar,
        text="Insertar Coordinación",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")
    
    frame_formulario = tk.Frame(coordinacion_insertar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    campos = [
        ("DNI", "DNI"),
        ("Nombres", "Nombres"),
        ("Apellidos", "Apellidos"),
        ("Correo", "Correo"),
    ]

    entradas = {}
    for idx, (etiqueta, clave) in enumerate(campos):
        tk.Label(
            frame_formulario,
            text=etiqueta,
            font=("Helvetica", 16),
            fg="black",
            bg="white"
        ).grid(row=idx, column=0, sticky="e", pady=5, padx=5)
        
        entrada = tk.Entry(frame_formulario, font=("Helvetica", 16), width=30)
        entrada.grid(row=idx, column=1, pady=5, padx=5)
        entradas[clave] = entrada
        frame_botones = tk.Frame(coordinacion_insertar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.8, anchor="center")
    
    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar_datos 
    )
    btn_guardar.grid(row=0, column=0, padx=10)
    
    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=coordinacion_insertar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)


#insertar transaccion
def insertar_Transaccion():
    def validar_datos():
        codigo_transaccion = entradas["Código de Transacción"].get().strip()
        monto_transaccion = entradas["Monto de transacción"].get().strip()
        tipo_transaccion = entradas["Tipo de Transacción"].get().strip()
        dni_alumno = entradas["DNI Alumno"].get().strip()
        dni_coordinacion = entradas["DNI Coordianción"].get().strip()

        if not codigo_transaccion.isalnum() or len(codigo_transaccion) != 8:
            messagebox.showerror("Error", "El Código de Transacción debe ser alfanumérico y tener exactamente 8 caracteres.")
            return
        try:
            monto = float(monto_transaccion)
            if monto <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El Monto de Transacción debe ser un número decimal mayor a 0.0")
            return
        if not tipo_transaccion:
            messagebox.showerror("Error", "El Tipo de Transacción no puede estar vacío.")
            return
        if not dni_alumno.isdigit() or len(dni_alumno) != 8:
            messagebox.showerror("Error", "El DNI del Alumno debe contener 8 dígitos numéricos.")
            return
        if not dni_coordinacion.isdigit() or len(dni_coordinacion) != 8:
            messagebox.showerror("Error", "El DNI de Coordinación debe contener 8 dígitos numéricos.")
            return
        messagebox.showinfo("Éxito", "Datos ingresados correctamente.")
    transaccion_insertar = tk.Toplevel()
    transaccion_insertar.title("Insertar Transacción")
    transaccion_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(transaccion_insertar)
    tk.Label(
        transaccion_insertar,
        text="Insertar Transacción",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")
    
    frame_formulario = tk.Frame(transaccion_insertar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    campos = [
        ("Código de Transacción", "Código de Transacción"),
        ("Monto de transacción", "Monto de transacción"),
        ("Tipo de Transacción", "Tipo de Transacción"),
        ("DNI Alumno", "DNI Alumno"),
        ("DNI Coordianción", "DNI Coordianción"),
    ]

    entradas = {}
    for idx, (etiqueta, clave) in enumerate(campos):
        tk.Label(
            frame_formulario,
            text=etiqueta,
            font=("Helvetica", 16),
            fg="black",
            bg="white"
        ).grid(row=idx, column=0, sticky="e", pady=5, padx=5)
        
        entrada = tk.Entry(frame_formulario, font=("Helvetica", 16), width=30)
        entrada.grid(row=idx, column=1, pady=5, padx=5)
        entradas[clave] = entrada
        frame_botones = tk.Frame(transaccion_insertar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.8, anchor="center")
    
    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar_datos
    )
    btn_guardar.grid(row=0, column=0, padx=10)
    
    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=transaccion_insertar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)

#insertar un recibo
def isnertar_recibo():
    def validar_datos():
        numero_recibo = entradas["Número de recibo"].get().strip()
        fecha_emision = entradas["Fecha de Emisión"].get().strip()
        nombres_alumno = entradas["Nombres del Alumno"].get().strip()
        razon_pago = entradas["Razón de Pago"].get().strip()
        codigo_transaccion = entradas["Código de Transacción"].get().strip()
        nombre_remitente = entradas["Nombre del remitente"].get().strip()
        monto_pago = entradas["Monto de pago"].get().strip()
        metodo_pago = entradas["Método de pago"].get().strip()
        dni_coordinacion = entradas["DNI Coordinación"].get().strip()
        
        if not numero_recibo.isalnum() or len(numero_recibo) != 6:
            messagebox.showerror("Error", "El Número de Recibo debe ser alfanumérico y tener exactamente 6 caracteres.")
            return
        if not validar_fecha(fecha_emision):
            messagebox.showerror("Error", "La Fecha de Emisión debe tener el formato dd/mm/yyyy.")
            return
        if not nombres_alumno.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Los Nombres del Alumno deben contener solo letras.")
            return
        if not razon_pago:
            messagebox.showerror("Error", "La Razón de Pago no puede estar vacía.")
            return
        if not codigo_transaccion.isalnum() or len(codigo_transaccion) != 8:
            messagebox.showerror("Error", "El Código de Transacción debe ser alfanumérico y tener exactamente 8 caracteres.")
            return
        if not nombre_remitente.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El Nombre del Remitente debe contener solo letras.")
            return
        try:
            monto = float(monto_pago)
            if monto <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "El Monto de Pago debe ser un número decimal mayor a 0.0")
            return
        if not metodo_pago.replace(" ", "").isalpha():
            messagebox.showerror("Error", "El Método de Pago debe contener solo letras")
            return
        if not dni_coordinacion.isdigit() or len(dni_coordinacion) != 8:
            messagebox.showerror("Error", "El DNI de Coordinación debe contener 8 dígitos numéricos.")
            return
        messagebox.showinfo("Éxito", "Datos ingresados correctamente")
    def validar_fecha(fecha):
        if len(fecha.split('-')) != 3:
            return False
        dia, mes, year = fecha.split('-')
        if not (dia.isdigit() and mes.isdigit() and year.isdigit()):
            return False
        dia, mes, year = int(dia), int(mes), int(year)
        return 1 <= dia <= 31 and 1 <= mes <= 12 and year > 1900
    
    recibo_insertar = tk.Toplevel()
    recibo_insertar.title("Insertar Recibo de Pago")
    recibo_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(recibo_insertar)
    tk.Label(
        recibo_insertar,
        text="Insertar Recibo de Pago",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")
    
    frame_formulario = tk.Frame(recibo_insertar, bg="white", bd=5, padx=20, pady=20)
    frame_formulario.place(relx=0.5, rely=0.5, anchor="center")
    campos = [
        ("Número de recibo", "Número de recibo"),
        ("Fecha de Emisión", "Fecha de Emisión"),
        ("Nombres del Alumno", "Nombres del Alumno"),
        ("Razón de Pago", "Razón de Pago"),
        ("Código de Transacción", "Código de Transacción"),
        ("Nombre del remitente", "Nombre del remitente"),
        ("Monto de pago", "Monto de pago"),
        ("Método de pago", "Método de pago"),
        ("DNI Coordinación", "DNI Coordinación"),
    ]

    entradas = {}
    for idx, (etiqueta, clave) in enumerate(campos):
        tk.Label(
            frame_formulario,
            text=etiqueta,
            font=("Helvetica", 16),
            fg="black",
            bg="white"
        ).grid(row=idx, column=0, sticky="e", pady=5, padx=5)
        
        entrada = tk.Entry(frame_formulario, font=("Helvetica", 16), width=30)
        entrada.grid(row=idx, column=1, pady=5, padx=5)
        entradas[clave] = entrada
        frame_botones = tk.Frame(recibo_insertar, bg="skyblue")
    frame_botones.place(relx=0.5, rely=0.8, anchor="center")
    
    btn_guardar = tk.Button(
        frame_botones,
        text="Guardar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=validar_datos
    )
    btn_guardar.grid(row=0, column=0, padx=10)
    
    btn_regresar = tk.Button(
        frame_botones,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=recibo_insertar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)
    
#menu insertar
def menu_insertar():
    ventana_insertar = tk.Toplevel()
    ventana_insertar.title("Menú de Inserción")
    ventana_insertar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(ventana_insertar)

    tk.Label(
        ventana_insertar,
        text="Menú de Inserción",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_opciones = tk.Frame(
        ventana_insertar,
        bg="white",
        bd=5,
        padx=20,
        pady=10
    )
    frame_opciones.place(relx=0.5, rely=0.5, anchor="center")

    opciones = [
        "1. Insertar Alumno",
        "2. Insertar Cursos",
        "3. Insertar Coordinación Academica",
        "4. Insertar Transacción",
        "5. Insertar Recibo de Pago",
    ]
    for opcion in opciones:
        tk.Label(
            frame_opciones,
            text=opcion,
            font=("Helvetica", 18),
            fg="black",
            bg="white",
        ).pack(pady=5)
        
    frame_input = tk.Frame(ventana_insertar, bg="white", bd=5, padx=20, pady=10)
    frame_input.place(relx=0.5, rely=0.8, anchor="center")
    global entrar_opc
    tk.Label(
        frame_input,
        text="Elige una opción: ",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).pack(side="left", padx=5)

    entrar_opc = tk.Entry(frame_input, font=("Helvetica", 16), width=5)
    entrar_opc.pack(side="left", padx=5)
    tk.Button(
        frame_input,
        text="Ok",
        font=("Arial", 14),
        bg="black",
        fg="white",
        command=opc_insertar
    ).pack(side="left", padx=5)  
    
    frame_boton = tk.Frame(ventana_insertar, bg="skyblue")
    frame_boton.place(relx=0.5, rely=0.9, anchor="center")
    btn_regresar = tk.Button(
        frame_boton,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=ventana_insertar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)



#menu modificar
def menu_modificar():
    ventana_modificar = tk.Toplevel()
    ventana_modificar.title("Menú de Modificación")
    ventana_modificar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(ventana_modificar)

    tk.Label(
        ventana_modificar,
        text="Menú de Modificación",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_opciones = tk.Frame(
        ventana_modificar,
        bg="white",
        bd=5,
        padx=20,
        pady=10
    )
    frame_opciones.place(relx=0.5, rely=0.5, anchor="center")

    opciones = [
        "1. Modificar Alumno",
        "2. Modificar Curso",
        "3. Modificar Coordinación",
        "4. Modificar Correo",
        "5. Modificar Telefóno Alumno",
        "6. Modificar Telefóno Coordinación"
    ]
    for opcion in opciones:
        tk.Label(
            frame_opciones,
            text=opcion,
            font=("Helvetica", 18),
            fg="black",
            bg="white",
        ).pack(pady=5)
        
    frame_input = tk.Frame(ventana_modificar, bg="white", bd=5, padx=20, pady=10)
    frame_input.place(relx=0.5, rely=0.8, anchor="center")
    global modificar_opc
    tk.Label(
        frame_input,
        text="Elige una opción: ",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).pack(side="left", padx=5)

    modificar_opc = tk.Entry(frame_input, font=("Helvetica", 16), width=5)
    modificar_opc.pack(side="left", padx=5)
    tk.Button(
        frame_input,
        text="Ok",
        font=("Arial", 14),
        bg="black",
        fg="white",
        command=opc_modificar
    ).pack(side="left", padx=5)  
    
    frame_boton = tk.Frame(ventana_modificar, bg="skyblue")
    frame_boton.place(relx=0.5, rely=0.9, anchor="center")
    btn_regresar = tk.Button(
        frame_boton,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=ventana_modificar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)

#menu de Eliminar
def menu_eliminar():
    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Menú de Eliminación")
    ventana_eliminar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(ventana_eliminar)

    tk.Label(
        ventana_eliminar,
        text="Menú de Eliminación",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_opciones = tk.Frame(
        ventana_eliminar,
        bg="white",
        bd=5,
        padx=20,
        pady=10
    )
    frame_opciones.place(relx=0.5, rely=0.5, anchor="center")

    opciones = [
        "1. Eliminar Curso"
    ]
    for opcion in opciones:
        tk.Label(
            frame_opciones,
            text=opcion,
            font=("Helvetica", 18),
            fg="black",
            bg="white",
        ).pack(pady=5)

 
    frame_input = tk.Frame(ventana_eliminar, bg="white", bd=5, padx=20, pady=10)
    frame_input.place(relx=0.5, rely=0.8, anchor="center")
    global eliminar_opc
    tk.Label(
        frame_input,
        text="Elige una opción: ",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).pack(side="left", padx=5)

    eliminar_opc = tk.Entry(frame_input, font=("Helvetica", 16), width=5)
    eliminar_opc.pack(side="left", padx=5)
    tk.Button(
        frame_input,
        text="Ok",
        font=("Arial", 14),
        bg="black",
        fg="white",
        command=opc_eliminar
    ).pack(side="left", padx=5)  
    
    frame_boton = tk.Frame(ventana_eliminar, bg="skyblue")
    frame_boton.place(relx=0.5, rely=0.9, anchor="center")
    btn_regresar = tk.Button(
        frame_boton,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=ventana_eliminar.destroy 
    )
    btn_regresar.grid(row=0, column=1, padx=10)
def menu_consultar():
    ventana_consultar = tk.Toplevel()
    ventana_consultar.title("Menú de Consultas")
    ventana_consultar.geometry(f"{screen_width}x{screen_height}")
    agregar_imagen_fondo(ventana_consultar)

    # Título
    tk.Label(
        ventana_consultar,
        text="Menú de Consultas",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_opciones = tk.Frame(
        ventana_consultar,
        bg="white",
        bd=5,
        padx=20,
        pady=10
    )
    frame_opciones.place(relx=0.5, rely=0.5, anchor="center")

    # Opciones de consultas
    consultas = [
        "1. Recibos de pago de un alumno",
        "2. Transacciones de un alumno",
        "3. Cursos inscritos por un alumno",
        "4. Verificar pago por recibo",
        "5. Listado de transacciones por tipo",
        "6. Recibos por coordinador",
        "7. Total de pagos por mes",
        "8. Pagos mayores a un monto",
        "9. Información de cursos por idioma",
        "10. Alumnos con múltiples números de celular"
    ]

    for consulta in consultas:
        tk.Label(
            frame_opciones,
            text=consulta,
            font=("Helvetica", 18),
            fg="black",
            bg="white",
        ).pack(pady=5)

    # Entrada para seleccionar la consulta
    frame_input = tk.Frame(ventana_consultar, bg="white", bd=5, padx=20, pady=10)
    frame_input.place(relx=0.5, rely=0.8, anchor="center")
    global entry_consulta
    tk.Label(
        frame_input,
        text="Elige una consulta (1-10):",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).pack(side="left", padx=5)

    entry_consulta = tk.Entry(frame_input, font=("Helvetica", 16), width=5)
    entry_consulta.pack(side="left", padx=5)

    tk.Button(
        frame_input,
        text="Ok",
        font=("Arial", 14),
        bg="black",
        fg="white",
        command=ejecutar_consulta
    ).pack(side="left", padx=5)

    # Botón para regresar
    frame_boton = tk.Frame(ventana_consultar, bg="skyblue")
    frame_boton.place(relx=0.5, rely=0.9, anchor="center")
    btn_regresar = tk.Button(
        frame_boton,
        text="Regresar",
        font=("Helvetica", 14, "bold"),
        bg="skyblue",
        fg="white",
        padx=20,
        pady=10,
        command=ventana_consultar.destroy
    )
    btn_regresar.grid(row=0, column=1, padx=10)

def ejecutar_consulta():
    opcion = entry_consulta.get()
    try:
        opcion = int(opcion)
        if 1 <= opcion <= 10:
            # Abrir conexión a la base de datos
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="smartdb"
            )

            if conexion.is_connected():
                cursor = conexion.cursor()

                # Opciones de procedimientos almacenados
                if opcion == 1:
                    dni = obtener_parametro("Ingrese el DNI del alumno:")
                    cursor.callproc("obtener_recibo_pago_alumno", [dni])
                elif opcion == 2:
                    dni = obtener_parametro("Ingrese el DNI del alumno:")
                    cursor.callproc("obtener_transacciones_alumno", [dni])
                elif opcion == 3:
                    dni = obtener_parametro("Ingrese el DNI del alumno:")
                    cursor.callproc("listar_cursos_alumno", [dni])
                elif opcion == 4:
                    numero_recibo = obtener_parametro("Ingrese el número de recibo:")
                    cursor.callproc("verificar_pago_recibo", [numero_recibo])
                elif opcion == 5:
                    tipo_transaccion = obtener_parametro("Ingrese el tipo de transacción:")
                    cursor.callproc("listado_transacciones", [tipo_transaccion])
                elif opcion == 6:
                    dni_coordinador = obtener_parametro("Ingrese el DNI del coordinador:")
                    cursor.callproc("recibos_por_coordinador", [dni_coordinador])
                elif opcion == 7:
                    mes = int(obtener_parametro("Ingrese el mes (1-12):"))
                    anio = int(obtener_parametro("Ingrese el año (e.g., 2024):"))
                    cursor.callproc("total_pagos_por_mes", [mes, anio])
                elif opcion == 8:
                    monto = float(obtener_parametro("Ingrese el monto mínimo:"))
                    cursor.callproc("pagos_mayores_a", [monto])
                elif opcion == 9:
                    idioma = obtener_parametro("Ingrese el idioma del curso:")
                    cursor.callproc("informacion_cursos", [idioma])
                elif opcion == 10:
                    cursor.callproc("obtener_celular_multiples")
                else:
                    raise ValueError

                # Obtener resultados y mostrarlos
                for result in cursor.stored_results():
                    datos = result.fetchall()
                    mostrar_resultados(datos)

            conexion.close()
        else:
            raise ValueError
    except Error as e:
        messagebox.showerror("Error de Base de Datos", f"Error al conectar o ejecutar la consulta: {e}")
    except ValueError:
        messagebox.showerror("Error", "Elige una opción válida entre 1 y 10")

def obtener_parametro(mensaje):
    return simpledialog.askstring("Entrada", mensaje)

def mostrar_resultados(datos):
    if datos:
        resultados = "\n".join([", ".join(map(str, fila)) for fila in datos])
        messagebox.showinfo("Resultados", resultados)
    else:
        messagebox.showinfo("Resultados", "No se encontraron datos.")

#menu principal
def menu():
    raiz.destroy()
    ventana_menu = tk.Tk()
    ventana_menu.title("Menú Principal")
    ventana_menu.geometry(f"{screen_width}x{screen_height}")
    cargar_imagen()
    agregar_imagen_fondo(ventana_menu)

    tk.Label(
        ventana_menu,
        text="Menú Principal",
        font=("Helvetica", 36, "bold"),
        fg="white",
        bg="black"
    ).place(relx=0.5, rely=0.1, anchor="center")

    frame_opciones = tk.Frame(
        ventana_menu,
        bg="white",
        bd=5,
        padx=20,
        pady=10
    )
    frame_opciones.place(relx=0.5, rely=0.5, anchor="center")


    opciones = [
        "1. Insertar",
        "2. Modificar",
        "3. Eliminar",
        "4. Consultar"
    ]

    for opcion in opciones:
        tk.Label(
            frame_opciones,
            text=opcion,
            font=("Helvetica", 18),
            fg="black",
            bg="white",
        ).pack(pady=5)

    global entry_opcion
    frame_input = tk.Frame(ventana_menu, bg="white", bd=5, padx=20, pady=10)
    frame_input.place(relx=0.5, rely=0.8, anchor="center")
    tk.Label(
        frame_input,
        text="Elige una opción: ",
        font=("Helvetica", 16),
        fg="black",
        bg="white"
    ).pack(side="left", padx=5)

    entry_opcion = tk.Entry(frame_input, font=("Helvetica", 16), width=5)
    entry_opcion.pack(side="left", padx=5)

    tk.Button(
        frame_input,
        text="Ok",
        font=("Arial", 14),
        bg="black",
        fg="white",
        command=manejar_opcion
    ).pack(side="left", padx=5)


raiz = tk.Tk()
raiz.title("Bienvenido a Centro Smart")
screen_width = raiz.winfo_screenwidth()
screen_height = raiz.winfo_screenheight()
raiz.geometry(f"{screen_width}x{screen_height}")

cargar_imagen()

agregar_imagen_fondo(raiz)

#bienvenida
tk.Label(
    raiz,
    text="¡Bienvenido a Centro Smart!",
    font=("Helvetica", 66, "bold"),
    fg="white",
    bg="black"
).place(relx=0.5, rely=0.5, anchor="center")

#ir al menu
tk.Button(
    raiz,
    text="Ingresar",
    font=("Arial", 20),
    bg="white",
    fg="black",
    command=menu
).place(relx=0.5, rely=0.6, anchor="center")

raiz.mainloop()
