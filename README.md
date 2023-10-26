# Reto_10
# Punto 1
1. Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.
```python
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
```
# Punto 2
2. Desarrollar un algoritmo que calcule el [producto punto](https://www.cuemath.com/algebra/dot-product/) de dos arreglos de números enteros (reales) de igual tamaño.
```python
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
print(f"El producto punto de {lista} y {lista2} es {product}")
```
# Punto 3

3. Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.
```python
# GRACIAS JUANES POR AYUDARME, CASI NO PUEDO XD
lista = []
Valores = 0
j = int(input("Ingresa la cantidad de valores: "))
for Valores in range (j):
    Valores = float(input("Ingrese un número real: "))
    lista.append(Valores)    
print(lista)
print(f"La cantidad de ceros que aparecen son: {lista.count(0)}")
```
# Punto 4
4. Revisar que son los algoritmos de *sorting*, entender *bubble-sort* ([enlace](https://www.geeksforgeeks.org/bubble-sort/) a implementación).
En computación y matemáticas un algoritmo de ordenamiento es un algoritmo que pone elementos de una lista o un vector en una secuencia dada por una relación de orden, es decir, el resultado de salida ha de ser una permutación —o reordenamiento— de la entrada que satisfaga la relación de orden dada.

