# Importamos la libreria matplotlib
import matplotlib.pyplot as plt

# La mayoría de los gráficos suelen tener dos ejes de coordenadas
#  para representar sus datos (x, y)
x = ['Betis', 'Atletico de Madrid', 'Barcelona', 'Real Madrid']
# Valor de mercado
y = [5, 10, 15, 8]

# Creamos el gráfico mediante plt y con un método iremos indicando
#  el tipo de gráfico que queremos.

# Barras
plt.bar(x, y)
# Podemos personalizar el gráfico
plt.title("Gráfico de barras")
# Leyenda para ejes
plt.xlabel("Equipos")
plt.ylabel("Valor de mercado")
# Podemos almacenar el gráfico en una imágen
plt.savefig('images/barras.png')
plt.show()
