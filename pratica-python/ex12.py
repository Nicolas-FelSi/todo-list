# Manipulação de arquivos

# Escreva um programa que leia um arquivo .txt com uma lista de nomes e exiba todos os nomes em ordem alfabética.

with open("pessoas.txt", "r", encoding="utf8") as arquivo:
    conteudo = arquivo.read().split()
    print(sorted(conteudo))