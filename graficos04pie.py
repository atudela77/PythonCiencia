import matplotlib.pyplot as plt

# Los gráficos de sectores o tartas (pie charts) tienen etiquetas
# y valores
etiquetas = ['Betis', 'Atletico de Madrid', 'Barcelona', 'Real Madrid']
# Valor de mercado
valores = [5, 2, 15, 8]

# Creamos el gráfico mediante plt y con un método iremos indicando
#  el tipo de gráfico que queremos.
plt.pie(valores, labels=etiquetas)
plt.title("Gráfico de sectores")
plt.savefig('images/sectores.png')
plt.show()
