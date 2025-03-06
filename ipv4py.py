def numips(start: str, end: str):
    lista_start = start.split('.')[::-1]
    lista_end = end.split('.')[::-1]
    print(f"Final: {lista_end}")
    print(f"Inicio: {lista_start}")
    lista_resta = []
    resto = 0
    for i in range(4):
        resta = int(lista_end[i]) - int(lista_start[i])
        if resta >= 0:
            lista_resta.append((resta % 256) - resto)
            resto = 0
        else:
            lista_resta.append((resta % 256) - resto)
            resto = 1
    resultado = 0
    for i in range(4):
        resultado = resultado + lista_resta[i] * (256**i)
    print(f"Resta: {lista_resta}")
    print(resultado)

    return


def main():
    inicio = "0.0.0.0"
    fin = "255.255.255.255"
    numips(inicio, fin)


main()
