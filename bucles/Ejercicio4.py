datos=[]
numero=0
letras=0
varios=0

dato=input("Ingrese los datos: ")
for i in dato:
    ascii = ord(i)
    if (ascii>= 65 and ascii <=90) or (ascii>=97 and ascii<=122):
        datos.append(i)
        letras+=1
    elif ascii>=48 and ascii<=57:
        datos.append(i)
        numero+=1
    else:
        varios+=1
print(f"La cantidad de datos tipo String son: {letras}")
print(f"La cantidad de datos tipo Numerico son: {numero}")
print(f"La cantidad de datos varios que no person agregados a la lista son: {varios}")
print(f"Su lista es: {datos}")