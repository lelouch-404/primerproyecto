#verificador de edad

#interfaz
import tkinter as tk

ventana = tk.Tk()
ventana.title("verificador de edad")
ventana.geometry("300x200")

historial = []



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
    
    if edad.strip()  ==  "":
        return "edad_vacia"
    
    try:
        edad = int(edad)
    except ValueError:
        return "edad_invalida"
    
    if edad < 13:
        return "nino"
    elif edad < 18:
        return "adolescente"
    else:
        return "adulto"
    
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

    elif resultado_logica == "nino":
        resultado.config(text="eres un niño", fg ="green")
        historial.append(f"{nombre} - niño")

    elif resultado_logica == "adolescente":
        resultado.config(text= "eres un adolescente",  fg="green")
        historial.append(f"{nombre} - adolescente")

    elif resultado_logica == "adulto":
        resultado.config(text= "eres un adulto", fg="green")
        historial.append(f"{nombre} - adulto")


def mostrar_historial():
    if not historial:
        resultado.config(text="No hay historial")
        return

    ventana_historial = tk.Toplevel()
    ventana_historial.title("Historial")
    ventana_historial.geometry("300x300")

    texto = "\n".join(historial)

    label_historial = tk.Label(ventana_historial, text=texto, justify="left")
    label_historial.pack(padx=10, pady=10)

boton = tk.Button(ventana, text="Verificar", command=verificar,width=25)
boton.grid(row=3,column=0,columnspan=2,pady=10)

boton = tk.Button(ventana, text="historial", command=mostrar_historial,width=25)
boton.grid(row=5,column=0,columnspan=2,pady=10)

ventana.mainloop()

