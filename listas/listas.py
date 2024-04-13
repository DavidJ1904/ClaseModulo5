#Listas

planetas = ["Mercurio" , "Venus" , "Tierra" , "Marte" , "Júpiter" , "Saturno" , "Urano" , "Neptuno"]
# print(planetas[-3])
# print(planetas[2: ])
# print(len(planetas))
# print(planetas(8))


#Trabajar con una lista de Numeros

gravedad_planeta = [0.378, 0.907, 1, 0.377, 2.36, 0.916,0.889,1.12]
peso_bus = 124054 #Newton, Tierra

print(f"En la Tirra, un autobus de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_planeta[0]} N ")


print(f"Lo mas Liviano que sería en un autobús en el sistema solar es {peso_bus * min(gravedad_planeta)} N")
print(f"Lo mas Pesado que sería un autobús en el sistema solar es {peso_bus* max(gravedad_planeta)} N")