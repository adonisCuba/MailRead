# Clase encargada de realizar la salva de los mensajes en la base de datos.

import mysql.connector


class DBConnection:
    # Contructor de la clase
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    # Método encargado de salvar en base datos

    def saveMessages(self, messages):
        # Conexión a la base de datos
        cnx = mysql.connector.connect(user=self.user, password=self.password,
                                      host=self.host,
                                      database=self.database)
        # Inserción en la base de datos
        cursor = cnx.cursor()
        for msg in messages:
            query = ("INSERT INTO mailRead.correos"
                     "(remitente, asunto, contenido)"
                     "VALUES(%(remitente)s, %(asunto)s, %(contenido)s)"
                     )
            cursor.execute(query, msg)
        cnx.commit()
        cursor.close()
        cnx.close()
