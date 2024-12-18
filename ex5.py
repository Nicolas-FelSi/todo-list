# 5. Dicionário de contatos
# Objetivo: Manipulação de dicionários.
# Enunciado:
# Crie um programa que funcione como uma agenda de contatos. Ele deve ter as seguintes opções:

# Adicionar um novo contato (nome e telefone).
# Remover um contato pelo nome.
# Listar todos os contatos.
# Buscar um contato pelo nome.
# Sair do programa.
# Use um loop para manter o programa rodando até o usuário decidir sair.

from time import sleep


lista_contatos = []

def adicionar_contato(nome, telefone):    
    lista_contatos.append({
        "nome": nome,
        "telefone": telefone
    })
    
def remover_contato(nome):
    lista_contatos.remove(nome)
    
def listar_contatos():
    for contato in lista_contatos:
        print(f"{contato['nome']} - {contato['telefone']}.")
    
def buscar_contato_por_nome(nome):
    indice = lista_contatos.index(nome)
    return lista_contatos[indice]
    

while True:
    opcao = int(input(("""
    1 - Adicionar contato.
    2 - Remover contato.
    3 - Listar contatos.
    4 - Buscar contato.
    5 - Sair.
    """)))
    
    if opcao == 1:
        nome = input("Digite um nome para o contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif opcao == 2:
        nome = input("Digite o nome do contato que quer remover: ")
        remover_contato(nome)
    elif opcao == 3:
        listar_contatos()
        
    elif opcao == 4:
        nome = input("Digite o nome do contato que quer buscar: ")
        buscar_contato_por_nome(nome)
        
    elif opcao == 5:
        print("Encerrando programa...")
        sleep(3)
        break
    else:
        print("Opção incorreta, tente novamente.")
    