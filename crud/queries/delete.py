import sqlite3


conection = sqlite3.connect("../python_sqlite.db")
cursor = conection.cursor()

cursor.execute("DROP TABLE empleados")

conection.close()
