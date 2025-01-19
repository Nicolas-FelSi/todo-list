# Operações básicas

# Faça um programa que receba dois números do usuário e exiba a soma, subtração, multiplicação e divisão deles.
# Condicionais simples

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

if numero2 != 0:
    divisao = numero1 / numero2
    divisao_inteira = numero1 // numero2
else:
    divisao = "Indefinida (divisão por zero)"
    divisao_inteira = "Indefinida (divisão por zero)"

print()
print(f"Soma entre {numero1} e {numero2} é {soma}")
print(f"Subtração entre {numero1} e {numero2} é {subtracao}")
print(f"Multiplicação entre {numero1} e {numero2} é {multiplicacao}")
print(f"Divisão entre {numero1} e {numero2} é {divisao:.2f}")
print(f"Divisão inteira entre {numero1} e {numero2} é {divisao_inteira}")

