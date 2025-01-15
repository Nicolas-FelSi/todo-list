# Operações básicas

# Faça um programa que receba dois números do usuário e exiba a soma, subtração, multiplicação e divisão deles.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero
divisao_inteira = primeiro_numero // segundo_numero

print(f"Soma entre {primeiro_numero} e {segundo_numero}: {soma}")
print(f"Subtração entre {primeiro_numero} e {segundo_numero}: {subtracao}")
print(f"Multiplicação entre {primeiro_numero} e {segundo_numero}: {multiplicacao}")
print(f"Divisão entre {primeiro_numero} e {segundo_numero}: {divisao:.3}")
print(f"Divisão inteira entre {primeiro_numero} e {segundo_numero}: {divisao_inteira}")