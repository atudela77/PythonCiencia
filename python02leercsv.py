import pandas as pd

print("Lectura CSV")

# Almacenamos los datos del CSV en un DataFrame
df = pd.read_csv('data/datos.csv')
print(df)
# Al ser un CSV, si no se indica un separador distinto a 
# la coma no separa.
# En el siguiente se inda el separador de punto y coma
df = pd.read_csv('data/datos.csv', delimiter=';')
print(df)
print("\n")
# Primeras 5 filas
# Toma la primera fila como cabecera, si no tuviera habría que indicarlo.
print("Primeras cinco filas")
print(df.head())
print("\n")
# Ordenamos por edad
df_sorted = df.sort_values('edad')
print("Filas ordenadas por edad")
print(df_sorted)
print("\n")
# Podemos recuperar datos estadísticos como por ej. la media de edad
media_edad = df['edad'].mean()
print(f"La media de edad es {media_edad}")
print("\n")
# Podemos agrupar por columnas y recuperar datos de los grupos
print("Datos agrupados por ocupacion y muestra número de personas")
df_grupo = df.groupby('ocupacion').size()
print(df_grupo)
