import smtplib
from smtplib import SMTP
import re
import time
import sched
from threading import Timer
import schedule
def job():
	print 'hello'
schedule.every().monday.at("21:26").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)