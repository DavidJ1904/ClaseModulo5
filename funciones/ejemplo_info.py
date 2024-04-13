def agregar_nombre(informacion, nombre_apellido):
    informacion.append(nombre_apellido)

def agregar_edad(informacion, año_actual, año_nacimiento):
    edad = año_actual - año_nacimiento
    informacion.append(edad)
