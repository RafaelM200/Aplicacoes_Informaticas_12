seg= float(input ( "Quantos segundos: "))
while not(seg>1 and seg<=60):
    seg = float(input("Escolha o valor entre 1 e 60: "))

min= float(input ( "Quantos minutos : "))
while not(min>1 and min<=60):
    min = float(input("Escolha o valor entre 1 e 60: "))

hor= float(input ( "Quantas horas : "))
while not(hor>1 and hor<=60):
    hor = float(input("Escolha o valor entre 1 e 60: "))

valor=seg+(min*60)+(hor*60)
print ( "O valor dos segundo", valor)