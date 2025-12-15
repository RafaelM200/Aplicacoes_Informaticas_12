
LInf=int(input("Qual o limite inferior\n"))

LSup=int(input("Qual o limite superior\n"))


while LSup > LInf:
    LSup = LInf + 1
    print("O intervalo é,")


if LInf > LSup:
    print("Os limites são invalidos")