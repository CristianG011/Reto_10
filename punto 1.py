def arreglo(*args):
    x = 0
    for num in lista:
        x += num
    x = x/len(lista)
    return x
if __name__ == "__main__":
    a = int(input("ingrese valor 1:"))
    b = int(input("Ingrese valor 2:"))
    c = int(input("Ingrese valor 3:"))
    lista = [a, b, c]
    promedio = arreglo(a, b, c)
print(f"El promedio del arreglo de reales es {promedio}.")