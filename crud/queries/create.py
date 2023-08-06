import sqlite3


conection = sqlite3.connect("./python_sqlite.db")
cursor = conection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

cursor.execute(
    """INSERT INTO movie VALUES
        ("Monty Python and the Holy Grail", 1975, 8.2),
        ("And Now for Something Completely Different", 1971, 7.5)
    """
)

conection.commit()

result = cursor.execute("SELECT * FROM movie")

print(result.fetchall())

conection.close()
