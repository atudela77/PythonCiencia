import matplotlib.pyplot as plt

print("Representar ventas de productos")
# productos = []
# ventas = []
# for _ in range(5):
#     print("Introduzca el nombre del producto:")
#     producto = input()
#     productos.append(producto)
#     print("Introduzca el total de ventas: ")
#     venta = int(input())
#     ventas.append(venta)
ventas = [212, 123, 544, 678, 900]
productos = ['Zapatillas', 'Zapatos', 'Pantalones', 'Cahquetas', 'Calcetines']
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
colors = ("orange", "cyan", "grey", "indigo", "beige")
plt.pie(ventas, labels=productos, shadow=True, explode=explode,
        colors=colors)
plt.title("Gráfico de ventas de productos")
plt.savefig('images/productos.png')
plt.show()
