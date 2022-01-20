import mysql.connector as conexao


db = conexao.connect(

    host="localhost",
    user="lucas",
    password="12345",
    database="curso"
)

"""

Inserindo dados numa tabela do banco

cursor.execute('INSERT INTO disciplina values("pedro")')


"""


cursor = db.cursor()

cursor.execute('INSERT INTO disciplina values("pedro")')