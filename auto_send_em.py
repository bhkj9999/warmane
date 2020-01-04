'''
@Author: Henry Zhang
@Date: 2020-01-02 11:07:04
@LastEditors  : Henry Zhang
@LastEditTime : 2020-01-02 18:40:58
@Github: https://github.com/bhkj9999
'''
import smtplib, time
from warmane_notification import md5, getAllPelement

try:
    from passwd import account, password 
    # import your credential of Gmail
    print("import Email account name and password successfully\n")
except:
    print("Error! Please set the account name and password in passwd.py first\n")

try:
    from Receiver import receiver
    # import your Receiver List
    print("import Receiver Address successfully\n")
except:
    print("Error! Please set the receiver list, please set your receiver list in receiver.py first\n")


def sendInfo(text):
    accountname = account
    accountpassword = password

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    subject = "Warmane Event Check On Los Angeles Time: " + time.ctime()

    try:
        Sendto = receiver
        msg = "Subject: {}\n\n{}".format(subject, text)
        server.login(accountname, accountpassword)
        server.sendmail(accountname, Sendto, msg)
        server.quit()
    except Exception as e:
        errorText = " Something Wrong \n" + str(e)
        msg = "Subject: {}\n\n{}".format(subject, errorText)

    return msg