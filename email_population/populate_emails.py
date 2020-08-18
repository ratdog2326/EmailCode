import smtplib
import ssl
import contextlib
import time
from email.mime.text import MIMEText
#note: email_input.txt should be in the same location as this script
port = 465

file = open('email_input.txt', 'r')
num_temp = file.readline()
mail_num = int(num_temp)
for x in range(0, mail_num):

    sender = file.readline()
    password = file.readline()
    receive = file.readline()
    subject = file.readline()
    body = file.readline()
    # remember, this is in seconds!
    sleeptime_temp = file.readline()
    sleeptime = int(sleeptime_temp)

    message = "Subject: "+subject+"\n"+body

    print("starting to send...")
    with contextlib.closing(smtplib.SMTP_SSL("smtp.gmail.com", port)) as server:
        server.login(sender, password)
        server.sendmail(sender, receive, message)#

    print ("sent email!")
    if x == 1:
        print("Done")
    else:
        print("sending next email in %s seconds..." % (sleeptime))
    time.sleep(sleeptime)


file.close()
