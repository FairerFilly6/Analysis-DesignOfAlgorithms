print("Multiplicación de enteros")
A = input("Entero A:")
B = input("Entero B:")

DigitosA = []
DigitosB = []

for digito in A:
    DigitosA.append(int(digito))

for digito in B:
    DigitosB.append(int(digito))

print(DigitosA)
print(DigitosB)
print("-------------------------------------------")

filas = []


for idxB,numeroB in enumerate(reversed(DigitosB)):
    filas.append([])
    acarreo = 0
    for idxA, numeroA in enumerate(reversed(DigitosA)): 
        res = (numeroA * numeroB) + acarreo
        entero = res % 10
        acarreo = int(res / 10)
        filas[idxB].insert(0, entero)
    if(idxB != 0):
        filas[idxB].extend([0] * idxB)


for filaNum in filas:
    print(filaNum)

resultado = []

SumaColumna = 0
acarreo = 0

while any(fila for fila in filas):
    SumaColumna = 0
    
    for fila in filas:
        
        if fila:
            SumaColumna += fila.pop()
    SumaColumna += acarreo
    enteroSuma = SumaColumna % 10
    acarreo = int(SumaColumna / 10)
            
    resultado.insert(0,enteroSuma)



print("-------------------------------------------")
print(f" = {resultado}")

