# Gráfico de linhas com matplotlib
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

import matplotlib.pyplot as plt

# Dados
disciplinas = ['Português', 'Matemática', 'Tecnologias', 'Inglês']
medias = [15.4, 17.3, 18.1, 13.3]

# Gráfico
plt.plot(disciplinas, medias, marker='o')
plt.grid()
plt.xlabel('Disciplinas')
plt.ylabel('Média')
plt.title('Médias das Disciplinas')
plt.show()