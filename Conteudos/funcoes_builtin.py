# Exemplos de funções internas do Python
# abs, ord, chr, bin, divmod, len, round
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

numeros=[1,3,5,7,8,6,10,56,23,4,14]
absoluto= abs (-4)
n_ordem=ord("A")
caracter=chr(64)
binario=bin(8)

quoc_resto=divmod(23,5)
n_itens=len(numeros)
num_arred=round(245.5690,1)

print ("abs(-4) =",absoluto)
print ( "ord(A)=", n_ordem)
print ( " chr( 64 ) =" ,caracter)
print ( "bin( 8) =" , binario)
print ( "divmod ( 23,5 ) =" , quoc_resto)
print ( "len(numeros ) =" ,n_itens)
print ( "round (245.5690,1) =", num_arred)