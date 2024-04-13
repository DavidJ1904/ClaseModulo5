frace = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")

contador = 0
for i in frace:
    if i == letra:
        contador+=1

print(f"La letra se repite {contador}")

print(frace.count(letra))