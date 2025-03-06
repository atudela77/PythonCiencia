import oracledb
import matplotlib.pyplot as plt

sql = '''
    SELECT h.nombre AS hospital, count(p.empleado_no) AS empleados
      FROM hospital h
 LEFT JOIN plantilla p
        ON h.hospital_cod = p.hospital_cod
  GROUP BY h.nombre
  ORDER BY empleados DESC
'''

conn = oracledb.connect(
    user="system",
    password="oracle",
    dsn="localhost:1521/xe"
)
cursor = conn.cursor()
cursor.execute(sql)
hospitales = []
empleados = []
for hospital, empleado in cursor:
    hospitales.append(hospital.title())
    empleados.append(empleado)
cursor.close()
conn.close()

plt.pie(empleados, labels=hospitales)
plt.title("Empleados por hospital")
plt.show()
