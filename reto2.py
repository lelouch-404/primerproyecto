import tkinter as tk

# lista de prueba
historial = [
    "Juan - adulto",
    "Ana - adolescente",
    "Luis - niño",
    "Pedro - adulto",
    "Sofia - adolescente",
    "Carlos - adulto"
]

ventana = tk.Tk()
ventana.title("Prueba Scroll")
ventana.geometry("300x200")


def mostrar_historial():

  

    ventana_historial = tk.Toplevel()
    ventana_historial.title("Historial")
    ventana_historial.geometry("300x300")

    texto = "\n" .join(historial)

    text_widget = tk.Text(ventana_historial)
    text_widget.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(ventana_historial, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.insert("1.0", texto)





boton = tk.Button(ventana, text="Ver historial", command=mostrar_historial)
boton.pack(pady=20)

ventana.mainloop()