import tkinter as tk

ventana = tk.Tk()
ventana.title("verificador de edad")
ventana.geometry("300x200")



label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1)

label_edad = tk.Label(ventana, text="Edad:")
label_edad.grid(row=1,column=0)

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1)

resultado = tk.Label(ventana, text="")
resultado.grid(row=2, column=0, columnspan=2)

def verificar():
    nombre = entrada_nombre.get()

    if nombre.strip() == "":
        resultado.config(text="Ingresa un nombre válido")
        return


    edad = entrada_edad.get()

    if edad.strip() == "":
        resultado.config(text="ingrese un numero valido")
        return

    try:
        edad = int(edad)

        if edad >= 18:
            resultado.config(text=f"{nombre}, eres mayor de edad")
        else:
            resultado.config(text=f"{nombre}, eres menor de edad")

    except ValueError:
        resultado.config(text="Edad inválida")


boton = tk.Button(ventana, text="Verificar", command=verificar)
boton.grid(row=3,column=0,columnspan=2,pady=10)

ventana.mainloop()