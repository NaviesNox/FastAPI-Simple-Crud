import sqlite3

conn = sqlite3.connect("test.db")  # nama file db sesuai yang dipakai di database.py
cursor = conn.cursor()

cursor.execute("SELECT * FROM items")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
