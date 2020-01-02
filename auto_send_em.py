'''
@Author: Henry Zhang
@Date: 2020-01-02 11:07:04
@LastEditors  : Henry Zhang
@LastEditTime : 2020-01-02 17:52:42
@Github: https://github.com/bhkj9999
'''
import smtplib
import time
from passwd import account, Password 
from warmane_notification import md5, getAllPelement
# import your credential of Gmail

from Receiver import receiver
# import your Receiver List

def sendInfo(text):
    accountname = account
    accountpassword = Password
    
    try:
        Sendto = receiver[0]
        subject = "Warmane Event Check On Los Angeles Time: " + time.ctime()
        msg = "Subject: {}\n\n{}".format(subject, text)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(accountname, accountpassword)
        server.sendmail(accountname, Sendto, msg)
        server.quit()
    except Exception as e:
        Sendto = receiver[0]
        subject = "Warmane Event Check On Los Angeles Time: " + time.ctime()
        errorText = " Something Wrong \n" + str(e)
        msg = "Subject: {}\n\n{}".format(subject, errorText)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(accountname, accountpassword)
        server.sendmail(accountname, Sendto, msg)
        server.quit()

    return msg