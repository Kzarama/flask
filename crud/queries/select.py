import sqlite3


conection = sqlite3.connect("./python_sqlite.db")
cursor = conection.cursor()

result = cursor.execute("SELECT * FROM empleados")

print(result.fetchall())

conection.close()
