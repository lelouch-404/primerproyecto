#guardar tu usuario y edad
continuar_programa = True

while continuar_programa:
    while True:
        try:
            edad = int(input("cual es tu edad?: "))
            break
        except:
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
    


        

