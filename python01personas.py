import pandas as pd

print("Ejemplo de DataFrame")

# Vamos a crear un diccionario con elementos que se llaman series
# No deja de ser un diccionario con valores que van correspondientes
#  entre ellos, aunque podrían no serlos.
datos = {
    'nombres': ['Lucia', 'Andre', 'Alex', 'Antonia'],
    'edad': [22, 17, 48, 70],
    'ciudad': ['Segovia', 'Parla', 'Madrid', 'Toledo']
    }
# Cada una de las líneas es una serie

# Almacenamos los datos en un DataFrame
df = pd.DataFrame(datos)
print("DF completo")
print(df)

# Podemos filtrar los datos de un DataFrame mediante la siguiente
#  sintaxis:
# df[df[COLUMNA] == valor]
df_filtrado = df[(df['edad'] > 30)]
print("DF Filtrado")
print(df_filtrado)

# Ordenar por una o variuas columnas
# df.sort_values(COLUMNA)   
df_sorted = df.sort_values(['edad', 'ciudad'])
print("DF Ordenado")
print(df_sorted)
