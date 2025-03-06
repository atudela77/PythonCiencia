import oracledb
import matplotlib.pyplot as plt

print("Gráficos con BBDD")
sql = '''
    select oficio, avg(salario) as media
    from emp
    group by oficio
'''
oficios = []
medias = []
conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
cursor = conn.cursor()
cursor.execute(sql)
for oficio, media in cursor:
    oficios.append(oficio)
    medias.append(media)
cursor.close()
conn.close()
plt.pie(medias, labels=oficios)
plt.title("Gráfico media salarial EMP")
plt.show()
