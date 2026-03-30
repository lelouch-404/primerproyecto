import tkinter as tk

ventana = tk.Tk()
ventana.title("verificador de edad")
ventana.geometry("300x200")



label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack()

entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

def verificar():
    nombre = entrada_nombre.get()


    edad = entrada_edad.get()

    try:
        edad = int(edad)

        if edad >= 18:
            resultado.config(text=f"{nombre}, eres mayor de edad")
        else:
            resultado.config(text=f"{nombre}, eres menor de edad")

    except ValueError:
        resultado.config(text="Edad inválida")


boton = tk.Button(ventana, text="Verificar", command=verificar)
boton.pack()

ventana.mainloop()