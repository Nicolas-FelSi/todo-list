import psycopg2


conexao = psycopg2.connect(database = "todolist",
                        user = "postgres",
                        host = "localhost",
                        password = "root",
                        port = 5432)

cursor = conexao.cursor()


# task = ("Estudar Flask", "Estudar primeiro python puro com postgresql")

# cursor.execute("INSERT INTO task (titulo, descricao) VALUES (%s, %s)", task)
# conexao.commit()

cursor.execute("SELECT * FROM task")
tasks = cursor.fetchall()

# id = 2
# cursor.execute("DELETE FROM task WHERE id = %s", id)
# conexao.commit()

# dados = ("status", id)
# cursor.execute("UPDATE task SET status = %s WHERE id = %s", dados)

# dados = ("titulo", id)
# cursor.execute("UPDATE task SET titulo = %s WHERE id = %s", dados)

# dados = ("descricao", id)
# cursor.execute("UPDATE task SET descricao = %s WHERE id = %s", dados)

cursor.close()
conexao.close()

print(tasks)