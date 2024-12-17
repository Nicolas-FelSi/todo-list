# 2. Cálculo de fatorial
# Objetivo: Praticar recursão ou laços de repetição.
# Enunciado:
# Crie uma função que receba um número inteiro positivo n e retorne o fatorial desse número.

# Exemplo:
# Entrada: 5
# Saída: 120 (5 x 4 x 3 x 2 x 1 = 120)

numero = int(input("Digite um número inteiro: "))


def calcular_fatorial(numero):
    resultado = numero
    
    for i in range(numero, 0, -1):
        if i == 1:
            resultado = resultado * (i)
        else:      
            resultado = resultado * (i-1)
    
    return resultado


for i in range(numero, 0, -1):   
    if i == 1:
        print(f"{i} = {calcular_fatorial(numero)}", end='')  
    else:      
        print(f"{i} x ", end='')
