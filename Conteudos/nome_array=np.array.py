# Criação de arrays NumPy a partir de listas e tuplos
# Disciplina: Aplicações Informáticas
# Autor: Rafael M.

import numpy as np

#Array criado a partir de uma list
print('Serras de Portugal')
serras=np.array(["Estrela","Monchique"])
print(serras)
"""Array criado a partir de um tuple e tipo de dados float"""
print('Portugal em km')
portugal_km=np.array((561,218,832,1215),dtype= float )
print(portugal_km)