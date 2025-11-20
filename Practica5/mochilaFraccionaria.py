import random as r

objetos = []
pesos = [20,50,60,100]
precios = [100, 200, 300, 50]
ganancia = 0
objetosMochila = []

#numeroObjetos = int(input("Ingresa el numero de objetos"))
mochila = int(input("Ingresa la capacidad de la mochila: "))
num_objetos = int(input("Ingresa el número de objetos: "))

for i in range(num_objetos):
    peso = r.randint(1, 100)      # peso aleatorio entre 1 y 100
    precio = r.randint(10, 500)   # precio aleatorio entre 10 y 500
    objetos.append((peso, precio))



pesoPrecio = [(peso, precio, precio / peso) for peso, precio in objetos]

pesoPrecio.sort(key= lambda x: x[2], reverse=True)

for peso, precio, valorpeso in pesoPrecio:
    if mochila == 0:
        break
    if peso <= mochila:
        ganancia += precio
        mochila -= peso
        objetosMochila.append((peso, precio))
    else:
        fraccion = mochila / peso
        ganancia += precio * fraccion
        objetosMochila.append((mochila, precio * fraccion))
        mochila = 0  # ya no cabe nada más





print(objetos)
print(pesoPrecio)
print("Los objetos que se ingresaron a la mochila")
print(objetosMochila)
print(f"Espacio vacio en la mochila {mochila}")






