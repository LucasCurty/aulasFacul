import sqlite3 as conector
import modelo

try:
    conexao = conector.connect('My_DB.db')
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    #Inserção de dados na tabela Marca
    comando1 = ''' INSERT INTO Marca (nome,sigla) VALUES (:nome,:sigla);'''

    marca1 = modelo.Marca("Marca A", "MA")
    cursor.execute(comando1, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = modelo.Marca("Marca B", "MB")
    cursor.execute(comando1, vars(marca2))
    marca2.id = cursor.lastrowid

#Inserção de dados na tabela Veiculo
    comando2 = '''INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
    veiculo1 = modelo.Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
    veiculo2 = modelo.Veiculo("BAA0001", 2002, "Preto", 1.4, 10000000099, marca1.id)
    veiculo3 = modelo.Veiculo("CAA0001", 2003, "Branco", 2.0, 20000000099, marca2.id)
    veiculo4 = modelo.Veiculo("DAA0001", 2004, "Branco", 2.2, 30000000099, marca2.id)
    cursor.execute(comando2,vars(veiculo1))
    cursor.execute(comando2,vars(veiculo2))
    cursor.execute(comando2,vars(veiculo3))
    cursor.execute(comando2,vars(veiculo4))
except conector.DatabaseError as error:
    print("Erro de banco de dados", error)
finally:
    if conexao:
        cursor.close()
        conexao.close()