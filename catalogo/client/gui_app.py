import tkinter as tk


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=False)
    barra_menu.add_cascade(label='inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear un registro')
    menu_inicio.add_command(label='Eliminar un registro')
    menu_inicio.add_command(label='Exit', command=root.destroy)

    menu_consulta = tk.Menu(barra_menu, tearoff=False)
    barra_menu.add_cascade(label='Consultas', menu=menu_consulta)

    menu_consulta.add_command(label='FAQ')
    menu_consulta.add_command(label="Contact'us")

    menu_config = tk.Menu(barra_menu, tearoff=False)
    menu_help = tk.Menu(barra_menu, tearoff=False)
    barra_menu.add_cascade(label='Configuracion', menu=menu_config)
    barra_menu.add_cascade(label='Help', menu=menu_help)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=800, height=500)
        self.root = root
        # Aca estoy usando la herencia como estoy heredando de frame directamente paso a empaquetar en vez de crear una insancia
        self.pack()
        # self.config(bg="#001c1f")
        self.campo_pelicula()

    def campo_pelicula(self):
        self.label_name = tk.Label(self, text="Name: ")
        self.label_name.config(font=('Arial', 12, 'bold'))
        self.label_name.grid(row=0, column=0, padx=10, pady=5)

        self.label_duration = tk.Label(self, text="Duration: ")
        self.label_duration.config(font=('Arial', 12, 'bold'))
        self.label_duration.grid(row=2, column=0, padx=10, pady=5)

        self.label_gender = tk.Label(self, text="Gender: ")
        self.label_gender.config(font=('Arial', 12, 'bold'))
        self.label_gender.grid(row=3, column=0, padx=10, pady=5)

        # Entradas de datos

        self.entry_name = tk.Entry(self)
        self.entry_name.config(width=50)
        self.entry_name.grid(row=0, column=1, padx=8, pady=5)

        self.entry_description = tk.Entry(self)
        self.entry_description.config(width=50)
        self.entry_description.grid(row=2, column=1, padx=8, pady=5)

        self.entry_gender = tk.Entry(self)
        self.entry_gender.config(width=50)
        self.entry_gender.grid(row=3, column=1, padx=8, pady=5)

        # Botones

        self.button_new = tk.Button(self, text="New", background="#001c1f")
        self.button_new.config(width=20, font=(
            'arial', 10, 'bold'), fg='white')
        self.button_new.grid(row=4, column=0)
