import smtplib
import ssl
import contextlib
import time
port = 465

sender = "wsupythontest@gmail.com"
password = "MuffinBox23"
receive = "wsupythontestalt@gmail.com"

message = """\
Subject: Test Subject

Test Body

"""

for x in range(0, 2):
    print("starting to send ", x)
    with contextlib.closing(smtplib.SMTP_SSL("smtp.gmail.com", port)) as server:
        server.login(sender, password)
        server.sendmail(sender, receive, message)

    print ("sent email!")
    time.sleep(300)
