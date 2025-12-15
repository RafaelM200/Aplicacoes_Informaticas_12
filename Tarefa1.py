
LInf=int(input("Qual o limite inferior\n"))

LSup=int(input("Qual o limite superior\n"))


while LSup > LInf:
    LInf= LInf + 1
    print("o valor é ",LInf)


if LInf > LSup:
    print("Os limites são invalidos")