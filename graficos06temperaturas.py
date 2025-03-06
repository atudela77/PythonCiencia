import matplotlib.pyplot as plt

# temperaturas = []
dias = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
# for dia in dias:
#     print(f"Introduzca la temperatura del {dia}:")
#     temperaturas.append(int(input()))
temperaturas1 = [12, 13, 11, 12, 14, 15, 15]
temperaturas2 = [14, 15, 16, 15, 17, 16, 18]
plt.plot(dias, temperaturas1, color='green', marker='x',
         linewidth=2, markersize=2)
plt.title("Temperatura de la semana")
plt.xlabel("Días")
plt.ylabel("Semana 1")
plt.plot(dias, temperaturas2, color='blue', marker='x',
         linewidth=2, markersize=2)
plt.ylabel("Semana 2")
plt.savefig("images/temperaturas.png")
plt.show()