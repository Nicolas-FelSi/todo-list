import psycopg2
from flask import Flask

conexao = psycopg2.connect(database = "todolist",
                        user = "postgres",
                        host = "localhost",
                        password = "root",
                        port = 5432)

cursor = conexao.cursor()

while True:
    opcao = input("""
                  1 - Criar tarefa
                  2 - Editar tarefa
                  3 - Listar tarefas
                  4 - Deletar tarefa
                  5 - Sair
                  """).strip()
    
    if opcao.isnumeric():
        opcao = int(opcao)
        
        if opcao == 1:
            task = {
                "titulo": input("Digite o titulo da tarefa: ").strip(),
                "descricao": input("Digite a descrição da tarefa: ").strip()
            }
            
            if len(task["titulo"]) != 0:
                cursor.execute("INSERT INTO task (titulo, descricao) VALUES (%s, %s)", (task["titulo"], task["descricao"]))
                conexao.commit()
                print()
                print("Tarefa criada com sucesso.")
            else:
                print()
                print("O título não pode estar vazio.")
            
        # elif opcao == 2:
        #     cursor.execute("SELECT * FROM task")
        #     tasks = cursor.fetchall()
            
        #     for task in tasks:
        #         print(f"{task[0]} - {task[1]} - {task[3]}")
            
        #     task_id = input("Digite o ID da tarefa que quer editar: ").strip()
            
        #     if task_id.isnumeric():
        #         task_id = int(task_id)
        #         cursor.execute("UPDATE task SET ")
                
        #     else:
        #         print("ID incorreto. Tente novamente.")
            
        elif opcao == 3:
            cursor.execute("SELECT * FROM task")
            tasks = cursor.fetchall()
            
            for task in tasks:
                print(f"{task[0]} - {task[1]} - {task[3]}")
        elif opcao == 4:
            cursor.execute("SELECT * FROM task")
            tasks = cursor.fetchall()
            
            for task in tasks:
                print(f"{task[0]} - {task[1]} - {task[3]}")
                
            id_task = input("Digite o ID da tarefa que quer deletar: ").strip()
            
            if id_task.isnumeric():
                id_task = int(id_task)
                cursor.execute("DELETE FROM task WHERE id = %s", id_task)
                conexao.commit()
            else:
                print("ID incorreto. Tente novamente.")
        elif opcao == 5:
            cursor.close()
            conexao.close()
            break
        else:
            print("Opção incorreta. Tente novamente!")

# dados = ("status", id)
# cursor.execute("UPDATE task SET status = %s WHERE id = %s", dados)

# dados = ("titulo", id)
# cursor.execute("UPDATE task SET titulo = %s WHERE id = %s", dados)

# dados = ("descricao", id)
# cursor.execute("UPDATE task SET descricao = %s WHERE id = %s", dados)


