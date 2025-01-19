# Intermediário - Introdução a Estruturas e Funções
# Funções

# Crie uma função que receba dois números como parâmetros e retorne o maior entre eles.

def encontrar_maior(*args):
    if args:
        return max(args)
    else:
        return "Nenhum número informado."

print(encontrar_maior(343, 543))

