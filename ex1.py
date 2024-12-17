# 1. Números pares e ímpares
# Objetivo: Desenvolver a lógica com laços de repetição e condicionais.
# Enunciado:
# Escreva um programa que receba um número inteiro positivo n do usuário e exiba todos os números pares e ímpares 
# entre 0 e n. Ao final, mostre a quantidade total de números pares e ímpares encontrados.

numero = int(input("Digite um número inteiro: "))
pares = []
impares = []
contador_par = 0
contador_impar = 0

for i in range(0, numero+1, 1):
    if i%2 == 0:
        pares.append(i)
        contador_par += 1
    else:
        impares.append(i)
        contador_impar += 1

print(f"Números pares entre 0 e {numero}: {pares}")
print(f"Números ímpares entre 0 e {numero}: {impares}")
print(f"{contador_par} números pares.")
print(f"{contador_impar} números ímpares.")