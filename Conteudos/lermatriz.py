# Criação e leitura de uma matriz com listas
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

def cria_matriz(num_linha, num_coluna):

    matriz = []
    for i in range(num_linha):
        linha = []
        for j in range(num_coluna):
            valor = int(input(f"Escreva o numero ({i})({j}): "))
            linha.append(valor)   # adiciona o valor à linha
        matriz.append(linha)     # adiciona a linha completa à matriz

    return matriz


def le_matriz():
    lin = int(input("Escreve o numero de linhas da matriz: "))
    col = int(input("Escreve o numero de colunas da matriz: "))
    return cria_matriz(lin, col)


# Programa principal
matriz = le_matriz()

print("\nMatriz:")
for linha in matriz:
    for valor in linha:
        print(valor, end=" ")
    print()