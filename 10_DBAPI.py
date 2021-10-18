import psycopg2
import sqlite3

DRIVER = 'sqlite3'
# DRIVER = 'psycopg2'


if DRIVER == 'psycopg2':
    connection = psycopg2.connect(user='admin', host='127.0.0.1', dbname='sqlalchemy', password='password')
else:
    connection = sqlite3.connect(':memory:')


print(f"connection is {type(connection)}")

cursor = connection.cursor()

print(f"cursor is {type(cursor)}")
# cursor.execute("rollback")

cursor.execute('CREATE TABLE schools ( id int, name varchar)')
cursor.execute("SELECT * FROM schools")
cursor.fetchall()
print(cursor.fetchall())

if DRIVER == 'psycopg2':
    cursor.execute("INSERT INTO schools (id, name) VALUES (%s, %s)", (100, "SRV School"))
else:
    cursor.execute("""INSERT INTO schools VALUES ('100','RVS School')""")

connection.commit()

cursor.execute("SELECT * FROM schools")
# cursor.fetchone()
print(cursor.fetchall())

cursor.execute('DROP TABLE schools')
connection.commit()

cursor.close()
connection.close()
