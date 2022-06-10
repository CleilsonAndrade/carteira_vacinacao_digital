import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO criancas (usuario, email, sexo, idade, vacina1) VALUES (?, ?, ?, ?, ?)",
            ('Usuario CRIANCA', 'crianca@teste.com', 'M', '1', 'nao')
            )

cur.execute("INSERT INTO adultos (usuario, email, sexo, idade, vacina1) VALUES (?, ?, ?, ?, ?)",
            ('Usuario ADULTO', 'adulto@teste.com', 'F', '2', 'sim')
            )

cur.execute("INSERT INTO idosos (usuario, email, sexo, idade, vacina1) VALUES (?, ?, ?, ?, ?)",
            ('Usuario IDOSO', 'idoso@teste.com', 'M', '3', 'nao')
            )

connection.commit()
connection.close()
