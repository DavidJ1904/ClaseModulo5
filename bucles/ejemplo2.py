def validar_numero(valor):
    return any(caracter.isdigit() for caracter in valor)

cantidad = int(input("Ingrese la cantidad de datos que desea ingresar: "))
datos = []
for i in range(cantidad):
        dato = input(f"Ingrese el dato #{i + 1}: ")

        if validar_numero(dato):
            try:
                dato_float = float(dato)
                datos.append(dato_float)
            except ValueError:
                datos.append(dato)
        else:
            datos.append(dato)

print(f"Su lista es: {datos}")
