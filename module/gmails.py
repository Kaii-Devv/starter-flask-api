import imaplib, re
import email as ma
from email.header import decode_header

class email:
    def __init__(self,mail,password):
        try:
            log = imaplib.IMAP4_SSL("imap.gmail.com")
            log.login(mail, password)
            log.select("inbox")
            status, messages = log.search(None, "ALL")
            message_ids = messages[0].split()
            message_ids.reverse()
            status, msg_data = log.fetch(message_ids[0], "(RFC822)")
            raw_email = msg_data[0][1]
            self.msg = ma.message_from_bytes(raw_email)
            self.sender, encoding = decode_header(self.msg.get("From"))[0]
            if isinstance(self.sender, bytes):
                self.sender = self.sender.decode(encoding if encoding else "utf-8")
            self.subject, encoding = decode_header(self.msg["Subject"])[0]
            if isinstance(self.subject, bytes):
                self.subject = self.subject.decode(encoding if encoding else "utf-8")
            self.msg = [ x.get_payload(decode=True).decode("utf-8") for x in self.msg.walk() if x.get_payload(decode=True)]
        except Exception as e : raise(e)

    
                
