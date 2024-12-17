# 3. Soma de elementos de uma lista
# Objetivo: Manipulação de listas e criação de funções.
# Enunciado:
# Escreva uma função que receba uma lista de números e retorne a soma de todos os elementos.

# Teste a função com uma lista fixa e outra lista preenchida pelo usuário.

lista = []

def somar_numeros_lista(lista):
    soma = 0
    
    for numero in lista:
        soma += numero
    
    return soma


while True:
    numero = int(input("Digite um número inteiro (0 para finalizar): "))
    
    if numero == 0:
        break
    
    lista.append(numero)
    

print(f"Soma total dos números da lista: {somar_numeros_lista(lista)}")