import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk

from menualumnoObjeto import AlumnoApp
from personal import PersonalApp
from materia import MateriaApp
from curso import CursoApp
from especialidad import EspecialidadApp
from nota import NotasApp
from asistencia import AsistenciaApp
from agenda import AgendaApp
import informacion
 


def open_personal_window():
    personal = tk.Toplevel(root)
    personal_app = PersonalApp(personal)
    
    
def open_alumno_window():
    alumno = tk.Toplevel(root)
    alumno_app = AlumnoApp(alumno)
    
    
def open_materia_window():
    materia = tk.Toplevel(root)
    materia_app = MateriaApp(materia)
    

def open_curso_window():
    curso = tk.Toplevel(root)
    curso_app = CursoApp(curso)
   
    
def open_especialidad_window():
    especialidad = tk.Toplevel(root)
    especialidad_app = EspecialidadApp(especialidad)
   

def open_nota_window():
    nota = tk.Toplevel(root)
    nota_app = NotasApp(nota)
 

def open_asistencia_window():
    asistencia = tk.Toplevel(root)
    asistencia_app = AsistenciaApp(asistencia)
    

def open_agenda_window():
    agenda = tk.Toplevel(root)
    agenda_app = AgendaApp(agenda)


def informacion1():    
    informacion.show_info()



root = tk.Tk()
root.title("Ventana Principal")
root.resizable(False, False)
root.geometry("400x400")
root.configure(bg="DodgerBlue4")
root.iconbitmap("logo.ico")

bg_image = ImageTk.PhotoImage(Image.open("logo2.jpg"))
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)


title_label = tk.Label(root, text="Sistema E.E.T N° 21", font=("Arial", 16), fg="white", bg="SteelBlue4")
title_label.pack(pady=10)


button_personal = tk.Button(root, text="Personal", command=open_personal_window)
button_personal.pack(pady=5, padx=20, fill=tk.X)


button_alumno = tk.Button(root, text="Alumno", command=open_alumno_window)
button_alumno.pack(pady=5, padx=20, fill=tk.X)


button_materia = tk.Button(root, text="Materia", command=open_materia_window)
button_materia.pack(pady=5, padx=20, fill=tk.X)

button_curso = tk.Button(root, text="Curso", command=open_curso_window)
button_curso.pack(pady=5, padx=20, fill=tk.X)


button_especialidad = tk.Button(root, text="Especialidad", command=open_especialidad_window)
button_especialidad.pack(pady=5, padx=20, fill=tk.X)

button_nota = tk.Button(root, text="Nota", command=open_nota_window)
button_nota.pack(pady=5, padx=20, fill=tk.X)


button_asistencia = tk.Button(root, text="Asistencia", command=open_asistencia_window)
button_asistencia.pack(pady=5, padx=20, fill=tk.X)


button_agenda = tk.Button(root, text="Agenda", command=open_agenda_window)
button_agenda.pack(pady=5, padx=20, fill=tk.X)

button_info_empresa = tk.Button(root, text="Mas Informacion", command=informacion1)
button_info_empresa.pack(pady=5, padx=20, fill=tk.X)



root.mainloop()
