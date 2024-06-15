import tkinter as tk


def show_info():
    root = tk.Tk()
    root.title("Informacion del Proyecto")
    root.geometry("900x600")
    root.configure(bg="gray11")
    root.iconbitmap("logo.ico")
    # Título
    title_label = tk.Label(root, text="Información del Proyecto", font=("Narrow", 20, "italic"), bg="gray11", fg="white")
    title_label.pack(pady=10)

    # Texto introductorio
    intro_text = """La escuela EET N° 21, un instituto dedicado a la educación técnica con una matricula 1200 alumnos,
    busca utilizar este software para gestionar de manera eficiente y ordenar la información tanto de sus estudiantes como del personal del establecimiento.
    La herramienta posibilita el almacenamiento, consulta, modificación y eliminación de datos,
    generando eficiencia en el uso del tiempo, espacio y mejorando el acceso a la información.
    La aplicacion fue desarrollada en el lenguaje Python, utilizando el paradigma de programación orientada a objetos (POO), aprovechando la sencillez y multiplataformidad del lenguaje.
    Se emplearon las bibliotecas pyodbc para la interacción con bases de datos mediante ODBC,
    y Tkinter para la creación de interfaces gráficas de usuario, especificando el diseño de la ventana,
    la disposición de la grilla, los widgets para la entrada de datos y botones para acciones específicas."""
    intro_label = tk.Text(root, wrap="word", font=("Arial", 14), bg="gray11", fg="white", height=11, width=100)
    intro_label.insert(tk.END, intro_text)
    intro_label.pack(pady=10)

    info_data = [
        "ALUMNO: GOMEZ PINATTI RODRIGO.",
        "PROFESOR: ING. VILLAFAÑE VICTOR.",
        "MATERIA: PRACTICA PROFESIONALIZANTE I.",
        "CARRERA: TECNICATURA SUPERIOR EN DESARROLLO DE SOFTWARE.",
        "AÑO: 2023."
    ]

    for data in info_data:
        key, value = data.split(":")
        label = tk.Label(root, text=f"{key.strip().upper()}: {value.strip()}", font=("Arial", 16, "bold"), bg="gray11", fg="white")
        label.pack(pady=10)

    root.mainloop()

