from mailReadClass import MailRead

mailRead = MailRead("imap.mail.com", "adonis.cuba@gmail.com", "Adogs*14901")
messages = mailRead.readMessage()
