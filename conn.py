import mysql.connector


def Conectar():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='DBPROJETO_INTEGRADOR'
    )


# conn = Conectar()
# cursor = conn.cursor()
# cursor.execute("SELECT NOME FROM IMIGRANTE")
# for nome in cursor.fetchall():
#     print(nome)
# conn.close()
