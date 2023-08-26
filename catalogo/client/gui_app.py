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
        self.moovie_field()
        self.disable_field()

    def moovie_field(self):
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
        self.my_name = tk.StringVar()
        self.entry_name = tk.Entry(self, textvariable=self.my_name)
        self.entry_name.config(width=50, font=('Arial', 12))
        self.entry_name.grid(row=0, column=1, padx=8, pady=5, columnspan=2)

        self.my_duration = tk.StringVar()
        self.entry_duration = tk.Entry(
            self, textvariable=self.my_duration)
        self.entry_duration.config(width=50, font=('Arial', 12))
        self.entry_duration.grid(
            row=2, column=1, padx=8, pady=5, columnspan=2)

        self.my_gender = tk.StringVar()
        self.entry_gender = tk.Entry(self, textvariable=self.my_gender)
        self.entry_gender.config(width=50, font=('Arial', 12))
        self.entry_gender.grid(row=3, column=1, padx=8, pady=5, columnspan=2)

        # Botones

        self.button_new = tk.Button(
            self, text="New", background="#E35FAF", command=self.enable_field)
        self.button_new.config(width=20, font=(
            'arial', 10, 'bold'), fg='#FFFFFF', cursor='hand2', activebackground='#692D51')
        self.button_new.grid(row=4, column=0, padx=10, pady=10)

        self.button_save = tk.Button(self, text="Save", background="#00C9F7", command=self.save_field)
        self.button_save.config(width=20, font=(
            'arial', 10, 'bold'), fg='#FFFFFF', cursor='hand2', activebackground='#002D37')
        self.button_save.grid(row=4, column=1, padx=10, pady=10)

        self.button_delete = tk.Button(
            self, text="Delete", background="#F7004A", command=self.disable_field)
        self.button_delete.config(width=20, font=(
            'arial', 10, 'bold'), fg='#FFFFFF', cursor='hand2', activebackground='#500010')
        self.button_delete.grid(row=4, column=2, padx=10, pady=10)

    def enable_field(self):

        self.my_name.set('')
        self.my_duration.set('')
        self.my_gender.set('')

        self.entry_name.config(state='normal')
        self.entry_duration.config(state='normal')
        self.entry_gender.config(state='normal')

        self.button_save.config(state='normal')
        self.button_delete.config(state='normal')

    def disable_field(self):
        self.my_name.set('')
        self.my_duration.set('')
        self.my_gender.set('')

        self.entry_name.config(state='disabled')
        self.entry_duration.config(state='disabled')
        self.entry_gender.config(state='disabled')

        self.button_save.config(state='disabled')
        self.button_delete.config(state='disabled')

    def save_field(self):
        
        self.disable_field()