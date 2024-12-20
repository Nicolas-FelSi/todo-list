# Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
# Na sequencia, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.

lista_bebidas = []

print("Quais são suas bebidas favoritas?")

for i in range(1, 6):
    bebida = input(f'{i} - ')
    lista_bebidas.append(bebida)


lista_ordenada = sorted(lista_bebidas)

for bebida in lista_ordenada:
    print(bebida)
