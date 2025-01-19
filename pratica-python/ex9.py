# Dicionários

# Crie um programa que armazene os nomes e idades de 3 pessoas em um dicionário. Depois, exiba quem é a pessoa mais velha.

lista_pessoas = []

for i in range(3):
    pessoa = {
        "nome": input("Digite seu nome: ").strip(),
        "idade": int(input("Digite sua idade: "))
    }
    
    lista_pessoas.append(pessoa)
    
    print()

pessoa_mais_velha = max(lista_pessoas, key=lambda pessoa: pessoa["idade"])

print(f"A pessoa mais velha é {pessoa_mais_velha['nome']} com {pessoa_mais_velha['idade']} anos")
