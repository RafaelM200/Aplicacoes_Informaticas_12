# Programa para mostrar o carácter correspondente ao código ASCII
# Caso o código não esteja entre 33 e 126, mostra mensagem de erro
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

# Leitura do código ASCII
codigo = int(input("Digite um código ASCII (33 a 126): "))

# Verificação do intervalo
if 33 <= codigo <= 126:
    print(f"O carácter correspondente ao código {codigo} é: '{chr(codigo)}'")
else:
    print("Indicou um código inválido")
