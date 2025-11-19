#El problema del cambio. Dar el cambio de una cantidad N en la menor cantidad de monedas; las monedas disponibles son {1, 5,10 y 25}. Prueba con diversos casos de N.


monto = int(input("Ingresa el monto a pagar:"))
pago = int(input("Ingresa el pago:"))

cambio = pago - monto

cambioFinal = cambio


monedas = [1,5,10,25]
monedasEntregadas = [0,0,0,0]
monedas.sort(reverse=True)

for k, moneda in enumerate(monedas):
    numMonedas = cambio // moneda
    
    cambio = cambio % moneda
    monedasEntregadas[k] = numMonedas
    

print(f"El cambio es de: {cambio}")

verificacionCambio = 0
for j in range(4):
    print(f" {monedasEntregadas[j]} monedas de {monedas[j]}")
    verificacionCambio += monedasEntregadas[j] * monedas[j]

print(f"Verificacion cambio: {verificacionCambio}")

if(verificacionCambio == cambioFinal):
    print("El cambio es correcto")
    

