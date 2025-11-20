import random as r

objetos = []
pesos = [20,50,60,100]
precios = [100, 200, 300, 50]
ganancia = 0
objetosMochila = []

#numeroObjetos = int(input("Ingresa el numero de objetos"))
mochila = int(input("Ingresa la capacidad de la mochila: "))
for peso, precio, in zip(pesos, precios):
    objetos.append((peso,precio))

pesoPrecio = [(peso, precio, precio / peso) for peso, precio in objetos]

pesoPrecio.sort(key= lambda x: x[2], reverse=True)
i = 0
while(pesoPrecio[i][0] <= mochila):
    ganancia += pesoPrecio[i][1]
    mochila -= pesoPrecio[i][0]
    objetosMochila.append(( pesoPrecio[i][0] ,  pesoPrecio[i][1]))
    i+=1
    if(pesoPrecio[i][0] > mochila):
        espacioDisp = mochila / pesoPrecio[i][0] 
        mochila += pesoPrecio[i][1] * espacioDisp
        mochila -= espacioDisp * pesoPrecio[i][0]




print(objetos)
print(pesoPrecio)
print("Los objetos que se ingresaron a la mochila")
print(objetosMochila)
print(f"Espacio vacio en la mochila {mochila}")






