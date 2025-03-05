import matplotlib.pyplot as plt

temperaturas = []
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
for dia in dias:
    print(f"Introduzca la temperatura del {dia}:")
    temperaturas.append(int(input()))
plt.plot(dias, temperaturas, color='green', marker='x',
         linewidth=2, markersize=2)
plt.title("Temperatura de la semana")
plt.xlabel("Días")
plt.ylabel("Temperatura")
plt.savefig("images/temperaturas.png")
plt.show()
