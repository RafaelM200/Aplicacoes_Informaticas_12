# Gráfico de barras com matplotlib
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

import matplotlib.pyplot as plt

# Dados
paises = ['Portugal', 'Brasil', 'Alemanha', 'França', 'Bélgica']
pontos = [10, 5, 7, 4, 9]  

# Gráfico
plt.bar(paises, pontos, color='blue', align='center')
plt.xlabel('Países')
plt.ylabel('Pontuação')
plt.title('Pontuação no Campeonato do Mundo de Futebol')
plt.show()