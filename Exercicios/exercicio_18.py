# Calculadora básica de duas variáveis
# Permite operações: +, -, *, /, //, %, **
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.
    
a=int(input("Qual o primeiro valor?\n"))
b=int(input("Qual o segundo valor?\n"))
c=(input("Qual a operacao logica(+, -, *, /, //, %, **)\n"))

if c == "+":
    op_adicao=a+b
    print("Adição -> ",a,"+",b,"=",op_adicao)

elif c == "-":
    op_subtracao=a-b
    print("Subtração -> ",a,"-",b,"=",op_subtracao)

elif c == "*":
    op_multiplicacao=a*b
    print("Multiplicação -> ",a, "x",b,"=", op_multiplicacao)

elif c == "/":
    op_divisao=a/b
    print("Divisão -> ",a,"/",b,"=",op_divisao)

elif c == "//":
    op_divisao_int=a//b
    print("Divisão inteira -> ",a,"//",b,"=",op_divisao_int)

elif c == "%":
    op_modulo_div=a%b
    print("Módulo -> ",a,"%", b, "=",op_modulo_div)

elif c == "**":
    op_exponenciacao=a**b
    print("Exponenciação -> ",a,"**",b,"=",op_exponenciacao)