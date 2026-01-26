import matplotlib.pyplot

matplotlib.pyplot.plot(["Jan.","Fev.","Mar.","Abr.","Mai.","Jun.","Jul.","Ago.","Set.","Out.","Nov.","Dez."],[9.03,9.78,12.37,13.99,16.78,20.39,20.54,22.92,20.48,16.84,12.28,9.75],"-o",color="purple", linewidth=3)

matplotlib.pyplot.title('Temperatura Média 1991–2019(Portugal Continental-Fonte IPMA)')

matplotlib.pyplot.ylabel('Temperatura (°C)')

matplotlib.pyplot.xlabel('Mês')

matplotlib.pyplot.grid()

matplotlib.pyplot.show()
