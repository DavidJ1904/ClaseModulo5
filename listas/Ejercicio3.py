menu=["Sopa de caracol","Estofado de res", "Sopa de verduras", "Carne aumada", "Encebollado", "Pescado frito" ]

opciones=input("\n Ingrese una de las opciones \n 1) Añadir plato al menú \n 2) Buscar en el menú \n 3) Eliminar plato del menú \n 4) Mostrar platos del menú \n")
if opciones == "1":
    agregar=input("Ingrese el pato a añadir al menu ")
    menu.append(agregar)
    print(menu)
elif opciones == "2":
    buscar=input("Ingrese el nombre del plato ")
    indice=menu.index(buscar)
    print(f"Su plato se emcuentra en el puesto {indice} del menú")
elif opciones == "3":
    eliminar=input("Ingrese el nombre del plato que dese eliminar ")
    menu.remove(eliminar)
    print(menu)
elif opciones == "4":
    print(menu)
else:
    print("La opción no es la correcta")
    