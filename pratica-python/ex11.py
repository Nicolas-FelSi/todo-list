# Simulando estruturas de dados

# Simule o comportamento de uma pilha (stack) usando uma lista: implemente as operações push, pop e peek.

pilha = []

while True:
    opcao = int(input("""
1 - Adicionar.
2 - Remover
3 - Consultar
4 - Sair
          """))
    
    print()
    
    if opcao == 1:
        carta = ""
        while len(carta) == 0:
            carta = input("Nome da carta para adicionar: ").strip()
            pilha.append(carta)
            print("Carta adicionada com sucesso.")
    elif opcao == 2:
        if len(pilha) == 0:
            print("Pilha vazia, adicione cartas para poder remover uma carta.")
        else:
            print(f"Carta {pilha[-1]} removida.")
            pilha.pop()
    elif opcao == 3:
        if len(pilha) != 0:
            print(f"Carta {pilha[-1]} no topo.")
        else:
            print("Pilha vazia, adicione cartas para poder consultar uma carta.")
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção errada.")