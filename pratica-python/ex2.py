# Operações básicas

# Faça um programa que receba dois números do usuário e exiba a soma, subtração, multiplicação e divisão deles.
# Condicionais simples

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtacao = numero1 - numero2
multiplicao = numero1 * numero2
divisao = numero1 / numero2
divisao_inteira = numero1 // numero2

print()
print(f"Soma entre {numero1} e {numero2} é {soma}")
print(f"Subtração entre {numero1} e {numero2} é {subtacao}")
print(f"Multiplicação entre {numero1} e {numero2} é {multiplicao}")
print(f"Divisão entre {numero1} e {numero2} é {divisao}")
print(f"Divisão inteira entre {numero1} e {numero2} é {divisao_inteira}")

