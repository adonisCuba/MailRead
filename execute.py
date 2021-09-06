from config import config
from mailReadClass import MailRead
from database import DBConnection

print("Leyendo correos del servidor")
# Creando instancia de la clase MailRead y obteniendo los mensajes
mailRead = MailRead(config["imapServer"],
                    config["mailUsername"], config["mailPassword"])
messages = mailRead.readMessage()

print("Salvando información en base de datos")
# Creando instancia de la clase DBConnection y salvando los mensajes obtenidos
db = DBConnection(config["databaseHost"],
                  config["databaseUser"], config["databasePassword"], config["databaseName"])

db.saveMessages(messages)
print("Tarea concluida")
