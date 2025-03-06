def numips(start: str, end: str):
    lista_start = start.split('.')[::-1]
    lista_end = end.split('.')[::-1]
    resto = 0
    resultado = 0
    for i in range(4):
        resultado += (((int(lista_end[i]) - int(lista_start[i]))%256)-resto)*(256**i)
        if (int(lista_end[i]) - int(lista_start[i])) >= 0:
            resto = 0
        else:
            resto = 1
    return resultado


def difips(start, end):
    ipstart = sum(int(x)*(256**(3-i)) for i, x in enumerate(start.split('.')))
    ipend = sum(int(x)*(256**(3-i)) for i, x in enumerate(end.split('.')))
    return ipend - ipstart


def main():
    inicio = "0.0.0.0"
    fin = "255.255.255.255"
    # inicio = "10.0.0.0"
    # fin = "10.0.0.10"
    print(numips(inicio, fin))
    print(difips(inicio, fin))


main()
