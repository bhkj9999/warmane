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
    md5 = warmane_notification.md5()
    Latest_Event_List = warmane_notification.getAllPelement()
    Latest_Event = Latest_Event_List[0]

    location = os.getcwd()
    sysstr = platform.system()

    if(sysstr == "Windows"):
        filePath = open(location + r"\recordExample.py", 'r+')
    else:
        filePath = open(location + "/recordExample.py", 'r+')

    if( recordExample.md5 != md5 ):
        auto_send_em.sendInfo("Latest Event Found \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event)
        print("Latest Event Found \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event)
        filePath.write("md5 = " + r'"' + md5 + r'"')
    else:
        # auto_send_em.sendInfo("Nothing Changed \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event)
        print("Nothing Changed \n\n" + "MD5 Check \n" + md5 + "\n" + "\n" + "The Latest Event is \n" + Latest_Event)
        filePath.write("md5 = " + r'"' + md5 + r'"')

    filePath.close()
    return 