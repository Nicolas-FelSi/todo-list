# Crie um programa que peça a idade do usuário e diga se ele é maior ou menor de idade.
# Laços de repetição básicos

idade_usuario = input("Digite sua idade: ")

if idade_usuario.isdigit():
    idade_usuario = int(idade_usuario)

    if idade_usuario >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")
else:
    print("Entrada inválida. Digite apenas números.")
