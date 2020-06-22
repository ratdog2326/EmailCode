import smtplib
import ssl
import contextlib
port = 465

sender = "wsupythontest@gmail.com"
password = "MuffinBox23"
receive = sender

message = """\
Subject: Test Subject

Test Body

"""

print("starting to send")
with contextlib.closing(smtplib.SMTP_SSL("smtp.gmail.com", port)) as server:
    server.login(sender, password)
    server.sendmail(sender, receive, message)

print ("sent email!")
