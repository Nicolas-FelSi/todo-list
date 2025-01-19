# Manipulação de strings

# Peça ao usuário para digitar uma frase e exiba:
# a) O número de palavras.
# b) A frase em maiúsculas e minúsculas.
# c) Se a palavra "Python" está na frase.

frase = input("Digite uma frase: ").strip()

print(f"Número de palavras: {len(frase.split())}")
print(f"Frase em maiúscula: {frase.upper()}")
print(f"Frase em minúscula: {frase.lower()}")
print(f"Python está na frase? {'Python' in frase}")

