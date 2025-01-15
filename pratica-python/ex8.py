# Laços e listas

# Gere uma lista de números de 1 a 20 usando um laço e exiba apenas os números pares.

from random import randint


lista_numeros = []
numeros_pares = []

for i in range(0, 20):
    lista_numeros.append(randint(1, 20))


for i in lista_numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
        
print(lista_numeros)
print(numeros_pares)
    