lista = []
Valores = 0
j = int(input("Ingresa la cantidad de valores: "))
for Valores in range (j):
    Valores = float(input("Ingrese un número real: "))
    lista.append(Valores)    
print(lista)
print(f"La cantidad de ceros que aparecen son: {lista.count(0)}")