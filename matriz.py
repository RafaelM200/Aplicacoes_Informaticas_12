def cria_matriz(num_linha, num_coluna):

    matriz=[]
    for i in range(num_linha):
        linha=[]
        for j in range(num_coluna):
            valor=int(input("Escreva o numero("+ str(i) + "](" + str(j) + ")"))
            matriz.append(valor)

    matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input("Escreve o numero de linhas da matriz: "))
    col = int(input("Escreve o numero de colunas da matriz: "))
    return cria_matriz(lin,col)

matriz = le_matriz()
print(matriz)