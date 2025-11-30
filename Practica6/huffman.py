
# text = input("Ingrese una cadena: ")

text = """Omar
Andrés
Barrón
Rivera
"""
size = len(text)

print(text)
print(size)

frecuencias = {}
for caracter in text:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1

print(frecuencias)

frecuencias = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)

print(frecuencias)
print("frecuencias usadas")
for frecuencia in frecuencias:
    print(frecuencia)







