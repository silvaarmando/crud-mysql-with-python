import mysql.connector

connection = mysql.connector.connect(
  host='localhost',
  user='armandosilva',
  password='10072304',
  database='students'
)

cursor = connection.cursor()

# DELETE
age = '20'
command = f'DELETE FROM students WHERE age = {age}'
cursor.execute(command)
connection.commit()

cursor.close()
connection.close()

# CREATE
name = "Armando"
age = 20
email = "armando@student.com"
command = f'INSERT INTO students (name, age, email) VALUES ("{name}", "{age}", "{email}")'
cursor.execute(command)
connection.commit()

# READ

command = f'SELECT * FROM students'
cursor.execute(command)
result = cursor.fetchall()
print(result)

# UPDATE

name = 'Armando'
email = 'armandosilva@student.com'
command = f'UPDATE students SET email = "{email}" WHERE name = "{name}"'
cursor.execute(command)
connection.commit()