#verificador de edad

def pedir_edad():
    while True:
        try:
            edad = int(input("cual es tu edad?: "))
            return edad
        except ValueError:
            print("ESO NO ES UN NUMERO")

def pedir_nombre():
    while True:
        nombre = input("cual es tu nombre: ")

        if nombre.strip() != "":
            return nombre
        else:
            print("por favor, ingresa un nombre valido")

def verificar_edad(nombre,edad):
    if edad >= 18:
        print(f"tu nombre es {nombre} ,eres mayor de edad")
                
    else:
        print(f"tu nombre es {nombre} ,eres menor de edad")



while True:

    while True:
        try:
    
            opciones = int(input("selecccione a continuacion: \n1. verificar edad\n2. salir"))
            break
        except ValueError:
            print("opcion incorrecta")


    if opciones == 1:
        edad = pedir_edad()
        nombre = pedir_nombre()
        verificar_edad(nombre,edad)
        
    elif opciones == 2:
        break

    else:
        print("elija una opcion valida")
