# Manipulação de strings

# Peça ao usuário para digitar uma frase e exiba:
# a) O número de palavras.
# b) A frase em maiúsculas e minúsculas.
# c) Se a palavra "Python" está na frase.

frase = input("Digite uma frase: ").strip()
frase_em_partes = frase.split()

print(f"Número de palavras: {len(frase_em_partes)}")
print(frase.upper())
print(frase.lower())
print("Python" in frase)

