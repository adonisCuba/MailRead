# Clase encargada de realizar la conexón al servidor de correo y la lectura de los nuevos correos
from imap_tools import MailBox, AND
import imap_tools


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
                    seen=False), mark_seen=False, bulk=True):
                messages.append(
                    {"uid": msg.uid, "remitente": msg.from_, "asunto": msg.subject, "contenido": msg.text})
        return messages

    # Método  encargado de marcar los mensajes previamente obtenidos como leídos
    def markAsRed(self, messages):
        uidMessages = []
        for msg in messages:
            uidMessages.append(msg["uid"])

        with MailBox(self.imapserver).login(self.username, self.password) as mailBox:
            mailBox.flag(uidMessages, (imap_tools.MailMessageFlags.SEEN), True)
