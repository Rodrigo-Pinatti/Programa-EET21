import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pyodbc
from PIL import Image, ImageTk

class AgendaApp:
    def __init__(self, root):
        #root.overrideredirect(True)
        self.root = root
        self.root.title("Gestión de Agendas")
        self.root.iconbitmap("logo.ico")
        #self.root.geometry("1300x600")
        self.root.resizable(True, True)
        self.root.configure(bg="DodgerBlue4")
        self.root.grid_propagate(True)
        
        
        
        
        self.conn = None
        self.tree = None

        self.create_widgets()
        self.connect_to_db()
        self.load_data()


   
    def create_widgets(self):
        frame_izquierda = tk.Frame(self.root, width=400, height=400, bg="DodgerBlue4")
        frame_izquierda.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        frame_derecha = tk.Frame(self.root, width=700, height=600, bg="DodgerBlue4")
        frame_derecha.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        self.create_data_entry_widgets(frame_izquierda)
        self.create_treeview_widget(frame_derecha)
        self.create_buttons(frame_izquierda)
        self.tree.bind("<<TreeviewSelect>>", self.load_data_to_entries)

    def create_data_entry_widgets(self, frame):
        labels = ["ID Agenda", "Descripcion", "Fecha", "Hora", "ID Personal"]
        self.entry_vars = {}
        for i, label_text in enumerate(labels):
            label = tk.Label(frame, text=label_text + ": ", bg="DodgerBlue4", fg="white")
            label.grid(row=i, column=0, sticky="e")
        
            entry_var = tk.StringVar()
            entry = tk.Entry(frame, textvariable=entry_var)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entry_vars[label_text] = entry_var

    def create_treeview_widget(self, frame):
        self.tree = ttk.Treeview(frame, columns=("ID Agenda", "Descripcion", "Fecha", "Hora", "ID Ppersonal"))
        self.tree.heading("#1", text="ID Agenda")
        self.tree.heading("#2", text="Descripcion")
        self.tree.heading("#3", text="Fecha")
        self.tree.heading("#4", text="Hora")
        self.tree.heading("#5", text="ID Personal")
        self.tree.grid()
        self.tree.column("#0", width=2)
        self.tree.column("#1", width=100)
        self.tree.column("#2", width=200)  # descripcion
        self.tree.column("#3", width=100)  # fecha
        self.tree.column("#4", width=100)  # hora
        self.tree.column("#5", width=100)  # id_personal

    def create_buttons(self, frame):
        agregar_button = tk.Button(frame, text="Agregar", command=self.agregar, width=10)
        agregar_button.grid(row=6, column=0, pady=10)

        borrar_button = tk.Button(frame, text="Borrar", command=self.borrar_registro, width=10)
        borrar_button.grid(row=6, column=1)

        modificar_button = tk.Button(frame, text="Modificar", command=self.modificar_registro, width=10)
        modificar_button.grid(row=6, column=2, padx=10)

        boton_conectar = tk.Button(frame, text="Refresh", command=self.refresh, width=10)
        boton_conectar.grid(row=7, column=0, padx=10)
        
        consultar_button = tk.Button(frame, text="Consultar", command=self.consultar_datos, width=10)
        consultar_button.grid(row=7, column=1, padx=10)
        
        salir_button = tk.Button(frame, text="Salir", command=self.salir, bg="red", fg="white", width=10)
        salir_button.grid(row=7, column=2, pady=10)
    """
    def connect_to_db(self):

        try:
            self.conn = pyodbc.connect('Driver={SQL Server};'
                                       'Server=Tssit01;'
                                       'Database=rodrigo1;'
                                       'UID=Soporte;'
                                       'PWD=Instituto_2023')
            messagebox.showinfo("Conexión Exitosa", "Conexión a la base de datos exitosa.")
        except Exception as e:
            messagebox.showerror("Error de Conexión", f"Error al conectar a la base de datos:\n{str(e)}")
     """ 
    def agregar(self):
        datos = {label: var.get() for label, var in self.entry_vars.items()}
        
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Agenda (descripcion, fecha, hora, id_personal) "
                           "VALUES (?, ?, ?, ?)",
                           (datos["Descripcion"], datos["Fecha"], datos["Hora"], datos["ID Personal"]))
            self.conn.commit()
            messagebox.showinfo("Registro Agregado", "El registro se ha agregado correctamente.")
            self.load_data()
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el registro:\n{str(e)}")

    def load_data_to_entries(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, 'values')
            keys_order = ["ID Agenda", "Descripcion","Fecha", "Hora", "ID Personal"]
            
            for i, key in enumerate(keys_order):
                if i < len(values):
                    var = self.entry_vars[key]
                    var.set(values[i])
                else:
                    var = self.entry_vars[key]
                    var.set("")

    def borrar_registro(self):
        id_a_borrar = self.entry_vars["ID Agenda"].get()

        if not id_a_borrar:
            messagebox.showerror("Error", "Ingrese un ID de agenda para borrar un registro.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM Agenda WHERE id_agenda=?", (id_a_borrar,))
            self.conn.commit()
            messagebox.showinfo("Registro Borrado", "El registro se ha borrado correctamente.")
            self.load_data()
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo borrar el registro:\n{str(e)}")

    def modificar_registro(self):
        datos = {label: var.get() for label, var in self.entry_vars.items()}
        id_a_modificar = datos["ID Agenda"]

        if not id_a_modificar:
            messagebox.showerror("Error", "Ingrese un ID de agenda para modificar un registro.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE Agenda SET descripcion=?, fecha=?, hora=?, id_personal=? WHERE id_agenda=?",
                           (datos["Descripcion"], datos["Fecha"], datos["Hora"], datos["ID Personal"], id_a_modificar))
            self.conn.commit()
            messagebox.showinfo("Registro Modificado", "El registro se ha modificado correctamente.")
            self.load_data()
            self.clear_entries()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el registro:\n{str(e)}")

    def consultar_datos(self):
        consulta = self.entry_vars["id_agenda"].get()

        if not consulta:
            messagebox.showerror("Error", "Ingrese un ID de agenda para buscar un registro.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT id_agenda, descripcion, fecha, hora, id_personal FROM Agenda WHERE id_agenda=?", (consulta,))
            result = cursor.fetchone()
            if result is not None:
                messagebox.showinfo("Registro encontrado", "El registro se ha encontrado correctamente.")
                self.tree.delete(*self.tree.get_children())  # Limpiar la Treeview
                self.tree.insert("", "end", values=(result[0], result[1], result[2], result[3], result[4]))
            else:
                messagebox.showinfo("No se encontraron resultados", "No se encontraron registros con el ID de agenda especificado.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo buscar el registro:\n{str(e)}")

    def refresh(self):
        self.load_data()
        self.clear_entries()

    def load_data(self):
        if self.conn is not None:
            cursor = self.conn.cursor()
            cursor.execute('SELECT id_agenda, descripcion, fecha, hora, id_personal FROM Agenda')
            data = cursor.fetchall()
            self.clear_treeview()
            for row in data:
                self.tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4]))

    def clear_entries(self):
        for var in self.entry_vars.values():
            var.set("")

    def clear_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def salir(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
