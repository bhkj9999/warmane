import smtplib
import time
from passwd import account, Password 
# import your credential of Gmail

from Receiver import receiver
# import your Receiver List


def AutoSendEmail():

    try:
        accountname = account
        accountpassword = Password

        error_title = "ERROR"
        send_error = "I'm waiting {idle} and I will try again."
        send_error_mail = "Mail invalid"
        send_error_char = "Invalid character"
        send_error_connection_1_2 = "Connection problem..."
        send_error_connection_2_2 = "Gmail server is down or internet connection is instabil."
        login_browser = "Please log in via your web browser and then try again."
        login_browser_info = "That browser and this software shood have same IP connection first time."

        mailDelay = 15
        exceptionDelay = 180

        Sendto = [receiver[0]]

        server = smtplib.SMTP("smtp.gmail.com", 587)

        server.ehlo()

        server.starttls()

        server.login(accountname, accountpassword)

        message = "FFFFF"

        server.sendmail(accountname, Sendto[0], message)

        server.quit()

    except Exception as e:
        e = str(e)
        if "the recipient address" in e and "is not a valid" in e:
            print(f"\n>>> {send_error_mail} [//> {Sendto}\n")
        elif "'ascii'" in e and "code can't encode characters" in e:
            print(f"\n>>> {send_error_char} [//> {Sendto}\n]")
        elif "Please" in e and "log in via your web browser" in e:
            print(f"\n>>> {login_browser}\n>>>  - {login_browser_info}")
            return
        elif "[WinError 10060]" in e:
            if "{idle}" in send_error:
                se = send_error.split("{idle}"); seMsg = f"{se[0]}{exceptionDelay} sec.{se[1]}"
            else:
                seMsg = send_error
            print(f"\n>>> {send_error_connection_1_2}\n>>> {send_error_connection_2_2}")
            print(f">>> {seMsg}\n")
            # Wait 5 minutes
            waitTime = exceptionDelay - mailDelay
            if waitTime <= 0:
                waitTime = exceptionDelay
                time.sleep(waitTime)
        else:
            if "{idle}" in send_error:
                se = send_error.split("{idle}"); seMsg = f"{se[0]}{exceptionDelay} sec.{se[1]}"
            else:
                seMsg = send_error
            print(f">>> {error_title} <<<", e)
            print(f">>> {seMsg}\n")
            # Wait 5 minutes
            time.sleep(exceptionDelay) 
            
    return