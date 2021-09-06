# Clase encargada de realizar la conexón al servidor de correo y la lectura de los nuevos correos
from imap_tools import MailBox, AND


class MailRead:
    # Constructor de la clase
    def __init__(self, imapServer, username, password):
        self.imapserver = imapServer
        self.username = username
        self.password = password
    # Método que obtiene y devuelve los mensajes no leídos

    def readMessage(self):
        messages = []
        # Conexión al servidor de correo
        with MailBox(self.imapserver).login(self.username, self.password) as mailBox:
            # Búsqueda de los correos sin leer.
            for msg in mailBox.fetch(criteria=AND(
                    seen=False), mark_seen=True, bulk=True):
                messages.append(
                    {"remitente": msg.from_, "asunto": msg.subject, "contenido": msg.text})
        return messages
