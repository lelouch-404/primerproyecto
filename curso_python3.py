import tkinter as tk

ventana = tk.Tk()
ventana.title("verificador de edad")
ventana.geometry("300x200")



label_nombre = tk.Label(ventana, text="Nombre:",font=("Arial", 14))
label_nombre.grid(row=0, column=0)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1)

label_edad = tk.Label(ventana, text="Edad:",font=("Arial", 14))
label_edad.grid(row=1,column=0)

entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1)

resultado = tk.Label(ventana, text="",font=("Arial",14))
resultado.grid(row=2, column=0, columnspan=2)

def evaluar_edad(nombre,edad):

    if nombre.strip() == "":
        return "nombre_error"
    
    if edad.strip() == "":
        return "edad_vacia"
    
    try:
        edad = int(edad)
    except ValueError:
        return "edad_invalida"
    
    if edad >= 18:
        return "mayor"
    else:
        return "menor"
    
def verificar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    resultado_logica = evaluar_edad(nombre, edad)

    if resultado_logica == "nombre_error":
        resultado.config(text="Ingresa un nombre válido", fg="orange")

    elif resultado_logica == "edad_vacia":
        resultado.config(text="Ingresa una edad", fg="orange")

    elif resultado_logica == "edad_invalida":
        resultado.config(text="Ingresa un número válido", fg="orange")

    elif resultado_logica == "mayor":
        resultado.config(text=f"{nombre}, eres mayor de edad", fg="green")

    elif resultado_logica == "menor":
        resultado.config(text=f"{nombre}, eres menor de edad", fg="red")


    


boton = tk.Button(ventana, text="Verificar", command=verificar,width=25)
boton.grid(row=3,column=0,columnspan=2,pady=10)

ventana.mainloop()