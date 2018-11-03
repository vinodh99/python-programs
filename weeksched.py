import smtplib
from smtplib import SMTP
import time
import schedule
def email_alert1():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'vin22pl@gmail.com'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
def email_alert2():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'praneeth1795@gmail.com'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
def email_alert3():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'banakapallisarat@gmail.com'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
def email_alert4():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'madhusudhan9kings@gmail.com'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
def email_alert5():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'sairamsubhash.ganti@sjsu.edu'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
def email_alert6():

    sender = 'vin22pl@gmail.com'
    password = 'vinsri851994'
    recipient = 'sreekar.adapa@gmail.com'  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: kitchen cleaning",
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n Hello,<br>This is just a reminder for your kitchen cleaning.</br><br><br> Thank you.</br></br><br><br>This is an auto generated email, please do not reply</br></br>")
    server.quit()
schedule.every().wednesday.at("19:46").do(email_alert1)
schedule.every().monday.at("22:00").do(email_alert2)
schedule.every().tuesday.at("22:00").do(email_alert3)
schedule.every().wednesday.at("22:00").do(email_alert4)
schedule.every().thursday.at("22:00").do(email_alert5)
schedule.every().friday.at("22:00").do(email_alert6)

while True:
    schedule.run_pending()
    time.sleep(1)