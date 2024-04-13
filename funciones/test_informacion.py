import informacion

parcientes = int(input("Ingrese la cantidad de pacientes: "))
for i in range (parcientes):
    print(f"Paciente numero {i}")
    nombre = input("Ingrese el nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    año = int(input("Ingrese el año de nacimiento del paciente: "))
    informacion.agregar_nombre(nombre,apellido)
    informacion.agregar_edad(año)
    print("\n")
    informacion.mostrar()