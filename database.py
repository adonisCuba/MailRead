import mysql.connector


class Connection:
    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def saveMessages(self, messages):
        cnx = mysql.connector.connect(self.user, self.password,
                                      self.host,
                                      self.database)
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
