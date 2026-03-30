#guardar tu usuario y edad

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
           




#menu interactivo 

while True:
    opciones_menu = int(input("elige lo siguiente: \n1. verificar edad\n2. salir\n"))
    if opciones_menu == 1:


        continuar_programa = True

        while continuar_programa:
            while True:
                try:
                    edad = int(input("cual es tu edad?: "))
                    break
                except ValueError:
                    print("ESO NO ES UN NUMERO")

            nombre = input("cual es tu nombre?: ")

            if edad >= 18:
                print(f"tu nombre es {nombre} y eres mayor de edad")
                
            else:
                print(f"tu nombre es {nombre} y eres menor de edad")
            respuesta = True

            while respuesta:
                respuesta = input("desea continuar? (si/no)")
            
                if respuesta.lower() != "si" and respuesta.lower() != "no":
                    print("esa no es una respuesta ") 
                    continue

                if respuesta.lower() == "si":
                    print("vamos de nuevo")
                    break
            
                if respuesta.lower() == "no":
                    print("es todo gracias")
                    continuar_programa = False
                    break

    elif opciones_menu == 2:
        break
        

        

