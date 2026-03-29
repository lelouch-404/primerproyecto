import secrets 
import string

while True:
    try:
        longitud = int(input("¿Cuántos caracteres quieres? "))
        break
    except:
        print("Ingresa un número válido")

while True:
    try:
        cantidad = int(input("¿Cuántas contraseñas quieres? "))
        break
    except:
        print("Ingresa un número válido")

nombre_archivo = input("¿Cómo quieres llamar el archivo? ")

caracteres = string.ascii_letters + string.digits + string.punctuation

with open(nombre_archivo + ".txt", "w") as archivo:
    for i in range(cantidad):
        password = ''.join(secrets.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña {i+1}: {password}")
        archivo.write(f"Contraseña {i+1}: {password}\n")


