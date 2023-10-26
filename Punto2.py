def producto(*args):
    p = 0
    for num in range(len(lista)):
        p += lista[num] * lista2[num]
    return p
if __name__ == "__main__":
    x = float(input("Ingrese el primer número de la primera lista: "))
    y = float(input("Ingrese el segundo número de la primera lista: "))
    a = float(input("Ingrese el primer número de la segunda lista: "))
    b = float(input("Ingrese el segundo número de la segunda lista: "))
    lista = [x, y]
    lista2 = [a, b]
    product = producto(x,y, a, b)
print(f"El profucto punto de {lista} y {lista2} es {product}")