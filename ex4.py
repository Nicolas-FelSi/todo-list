# 4. Contagem de vogais em uma string
# Objetivo: Manipulação de strings e laços de repetição.
# Enunciado:
# Escreva um programa que receba uma frase do usuário e conte quantas vogais existem nela.

# Dica: Considere as vogais "a", "e", "i", "o", "u" e suas versões maiúsculas.

frase = input("Digite uma frase ou palavra: ").lower()

vogais = ["a","e","i","o","u"]

contador = 0

for letra in frase:
    if letra in vogais:
        contador += 1

print(f"A frase \"{frase}\" contém {contador} vogais.")