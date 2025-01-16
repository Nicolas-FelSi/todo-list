# Dicionários

# Crie um programa que armazene os nomes e idades de 3 pessoas em um dicionário. Depois, exiba quem é a pessoa mais velha.

lista_pessoas = []

for i in range(0, 3):
    pessoa = {
        "nome": input("Digite seu nome: ").strip(),
        "idade": int(input("Digite sua idade: "))
    }
    
    lista_pessoas.append(pessoa)
    
    print()
    
pessoa_velha = max(lista_pessoas, key=lambda pessoa: pessoa["idade"])
    
print(f"Pessoa mais velha: {pessoa_velha["nome"]} com {pessoa_velha["idade"]} anos")