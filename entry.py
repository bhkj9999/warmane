'''
@Author: Henry Zhang
@Date: 2020-01-02 15:01:05
@LastEditors  : Henry Zhang
@LastEditTime : 2020-01-02 18:17:54
@Github: https://github.com/bhkj9999
'''

import warmane_notification
import auto_send_em
import recordExample
import os, time, platform


def saveToFile():
    url = 'https://www.warmane.com/'
    
    md5 = warmane_notification.md5(url)
    Latest_Event_List = warmane_notification.getAllPelement(url)
    Latest_Event = Latest_Event_List[0] if Latest_Event_List else 'Error'

    location = os.getcwd()
    sysstr = platform.system()

    if(sysstr == "Windows"):
        filePath = open(location + r"\recordExample.py", 'r+')
        errorFilePath = open(location + r"\error.txt", 'r+')
    else:
        filePath = open(location + "/recordExample.py", 'r+')
        errorFilePath = open(location + "/error.txt", 'r+')

    request_status_code = warmane_notification.getFormattedRes(url)[1]

    if( request_status_code == 200 ):
        if( recordExample.md5 != md5 ):
            auto_send_em.sendInfo("Latest Event Found \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event)
            print("Latest Event Found \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event)
            filePath.write("md5 = " + r'"' + md5 + r'"')
        else:
            print("Nothing Changed \n\n" + "MD5 Check \n" + md5 + "\n" + "\n" + "The Latest Event is \n" + Latest_Event)
    else:
        errorFilePath.write('Request Error ' + str(request_status_code))

    filePath.close()
    errorFilePath.close()

    equal = (md5 == recordExample.md5)

    return request_status_code, md5, recordExample.md5, equal


saveToFile()