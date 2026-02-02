# Exemplo da elaboração de um gráfico utilizando funções do módulo pyplot da biblioteca matplotlib
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.


# Importação do módulo pyplot da biblioteca matplotlib
import matplotlib.pyplot as plt

# Listas de valores a ser apresentados no gráfico
meses = ["Jan.", "Fev.", "Mar.", "Abr.", "Maio", "Jun.", "Jul.", "Ago.","Set.", "Out.", "Nov.", "Dez."]
temperaturas = [9.03, 9.78, 12.37, 13.99, 16.78, 20.39, 22.54, 22.92,20.48, 16.84, 12.28, 9.75]

# Cria o gráfico
plt.plot(meses, temperaturas, '-o', color="purple", linewidth=3)

# Apresenta o título do gráfico
plt.title('Temperatura Média 1991-2019 (Portugal Continental-Fonte IPMA)')

# Apresente o rótulo do eixo y
plt.ylabel('Temperatura (°C)')

# Apresente o rótulo do eixo x
plt.xlabel('Mês')

# Apresenta a grelha do gráfico
plt.grid()

# Apresenta o gráfico numa janela
plt.show()
