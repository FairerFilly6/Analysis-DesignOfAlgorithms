import random as r
n = int(input("Ingrese el numero de actividades: "))
actividades = []
horario = []

for i in range(n):
    inicio = r.randint(0,22)
    fin = r.randint(inicio + 1, 23)
    actividades.append((inicio, fin))

print(actividades)

actividades.sort(key=lambda x : x[1])
print(actividades)


i = 0
while(i < len(actividades) - 1):
    inicio =  actividades[i][0]
    fin = actividades[i][1]

    inicioSig = actividades[i+1][0]

    if(inicioSig < fin):
        actividades.pop(i+1)
    else:
        i+=1

print("Actividades disponibles:")
print(actividades)
    
