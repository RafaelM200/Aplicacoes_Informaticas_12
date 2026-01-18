# Operações aritméticas (adição e multiplicação)
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.


# Leitura dos dois números 
a1 = int(input("Qual o primeiro valor:"))
a2 = int(input("Qual o segundo valor:"))

# Menu de opções
print("Menu de operações:")
print("A - Adição")
print("M - Multiplicação")

op = input("Qual a operacao desejada:")

# Definição das funções
def adicao(a1, a2):
    return a1 + a2

def multiplicacao(a1, a2):
    return a1 * a2

if op.upper() == "A":
    resultado = adicao(a1, a2)
    print("O valor da adicao é", resultado)
elif op.upper() == "M":
    resultado = multiplicacao(a1, a2)
    print("O valor da multiplicacao é", resultado)
else:
    print("Operacao invalida")
