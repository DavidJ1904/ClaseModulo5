localidad=input("Ingrese el pais donde esta ")
#Ecuador
if localidad == "Ecuador":
    print("Bienvenido a Ecuador")
    Zona= input("Ingrese la zona en la que se encuentra ")
    #Zona urbana
    if Zona == "urbana":
        print("La velocidad máxima es 50Km/h y el mínimo 10Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <10:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >50:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
    #Zona rural
    elif Zona == "rural":
        print("La velocidad máxima es 70Km/h y el mínimo 51Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <51:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >70:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
    #Zona perimetral
    elif Zona == "perimetral":
        print("La velocidad máxima es 90Km/h y el mínimo 71Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <71:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >90:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
#Colombia
elif localidad == "Colombia":
     print("Bienvenido a Colombia")
     Zona= input("Ingrese la zona en la que se encuentra ")
     #Zona urbana
     if Zona == "urbana":
        print("La velocidad máxima es 30Km/h y el mínimo 10Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <10:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >30:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
     #Zona rural
     elif Zona == "rural":
        print("La velocidad máxima es 80Km/h y el mínimo 31Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <31:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >80:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
     #Zona perimetral
     elif Zona == "perimetral":
        print("La velocidad máxima es 100Km/h y el mínimo 81Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <81:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >100:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
#Perú
elif localidad == "Perú":
     print("Bienvenido a Perú")
     Zona= input("Ingrese la zona en la que se encuentra ")
     #Zona urbana
     if Zona == "urbana":
        print("La velocidad máxima es 40Km/h y el mínimo 10Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <10:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >40:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
     #Zona rural
     elif Zona == "rural":
        print("La velocidad máxima es 60Km/h y el mínimo 41Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <41:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >60:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
     #Zona perimetral
     elif Zona == "perimetral":
        print("La velocidad máxima es 120Km/h y el mínimo 61Km/h")
        velocidad=int(input("Ingrese su velocidad "))
        if velocidad <61:
            print(f"Su velocidad es {velocidad}Km/h es inferior a la minima \nAcelere un poco mas")
        elif velocidad >120:
            print(f"Su velocidad es {velocidad}Km/h es superior a la maxima \nDesacelere un poco")
        else:
            print(f"Su velocidad es {velocidad}km/h no es superior a la maxima, ni inferior a la minima \nMantenga su velocidad")
else:
    print("País no encontrado")