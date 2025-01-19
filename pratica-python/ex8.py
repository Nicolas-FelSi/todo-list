# Laços e listas

# Gere uma lista de números de 1 a 20 usando um laço e exiba apenas os números pares.

from random import randint


numeros_pares = [randint(1, 20) for _ in range(21) if randint(1, 20) % 2 == 0]

# for i in range(21):
#     numero = randint(1, 20)
    
#     if numero % 2 == 0:
#         numeros_pares.append(numero)


print(numeros_pares) 

