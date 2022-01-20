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

Lendo dados de uma tabela


cursor.execute("SELECT * FROM disciplina")
cursor.execute("SELECT * FROM disciplina")

dados = cursor.fetchall()


print(dados)

"""


cursor = db.cursor()

cursor.execute("SELECT * FROM disciplina")

dados = cursor.fetchall()


print(dados)