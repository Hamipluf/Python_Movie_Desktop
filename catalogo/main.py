import tkinter as tk
from client.gui_app import Frame, barra_menu


def main():
    root = tk.Tk()
    root.title("Catalogo de peliculas")
    root.iconbitmap(
        r"C:\Users\ramir\Desktop\programacion\Python Products\catalogo\img\popcorn.ico")
    # Esto indica que la ventana va a atomar el tamaño del frame
    root.resizable(0, 0)
    app = Frame(root=root)
    barra_menu(root=root)
    app.mainloop()


if __name__ == '__main__':
    main()
