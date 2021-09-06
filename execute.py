from config import config
from mailReadClass import MailRead
from database import Connection
print("Leyendo correos del servidor")
mailRead = MailRead(config["imapServer"],
                    config["mailUsername"], config["mailPassword"])
messages = mailRead.readMessage()

print("Salvando información en base de datos")
db = Connection(config["databaseHost"],
                config["databaseUser"], config["databasePassword"], config["databaseName"])

db.saveMessages(messages)
print("Tarea concluida")
