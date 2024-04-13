import ejemplo_info

def paciente_mayor(listas_nombres, listas_edades):
    mayor =listas_edades.index(max(listas_edades))
    return listas_nombres[mayor], listas_edades[mayor]

def paciente_menor(listas_nombres, listas_edades):
    menor =listas_edades.index(min(listas_edades))
    return listas_nombres[menor], listas_edades[menor]

nombres=[]
edades=[]

año_actual= int(input("Ingrese el año actual: "))
while True:
    mensaje=input("Ingrese el nombre y apellido de los pacientes conjunto con el año de nacimiento,\nsi acabó de ingresar los datos escriba terminado: ")
    if mensaje.lower() == "terminado":
       break
    nombre_apellido, año_nacimiento = mensaje.rsplit(' ',1)
    ejemplo_info.agregar_nombre(nombres, nombre_apellido)
    ejemplo_info.agregar_edad(edades, año_actual, int(año_nacimiento))

print("Lista de pacientes: ")
print(nombres)
print("Lista de edades de los pacientes: ")
print(edades)

paciente_mayor_nombre, paciente_mayor_edad = paciente_mayor(nombres, edades)
paciente_menor_nombre, paciente_menor_edad = paciente_menor(nombres, edades)
print(f"{paciente_mayor_nombre} con la edad de {paciente_mayor_edad} años es mayor a los demás pacientes.")
print(f"{paciente_menor_nombre} con la edad de {paciente_menor_edad} años es menor a los demás pacientes.")
