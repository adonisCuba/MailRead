from messageClass import Message
from imap_tools import MailBox, AND


class MailRead:
    def __init__(self, imapServer, username, password):
        self.imapserver = imapServer
        self.username = username
        self.password = password

    def readMessage(self):
        messages = []
        with MailBox(self.imapserver).login(self.username, self.password) as mailBox:
            for msg in mailBox.fetch(criteria=AND(
                    seen=False), mark_seen=False, bulk=True):
                messages.append(Message(msg.from_, msg.subject, msg.text))
                print(msg.from_, ':', msg.subject)
