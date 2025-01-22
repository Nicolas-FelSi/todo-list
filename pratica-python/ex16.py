# Conecte-se a um banco de dados SQLite, crie uma tabela de produtos e faça inserções e consultas.

import sqlite3


conexao = sqlite3.connect("produtos.db")

cursor = conexao.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS produto(categoria, nome, preco)")

cursor.execute("""
    INSERT INTO produto ('categoria', 'nome', 'preco') VALUES 
    ('Fruta', 'Banana', '4,99'),
    ('Fruta', 'Maçã', '2,50'),
    ('Eletrônico', 'Pendrive', '12,75')        
""")
conexao.commit()

cursor.execute("SELECT * FROM produto")
print(cursor.fetchall())
