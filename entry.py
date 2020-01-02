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
import os, time


def saveToFile():
    md5 = warmane_notification.md5()
    Latest_Event_List = warmane_notification.getAllPelement()
    Latest_Event = Latest_Event_List[0]

    # location = os.getcwd()
    # file = open(location + "/record "  + time.ctime() + ".txt", 'a')
    if(recordExample.md5 != md5 and recordExample.content != Latest_Event ):
        auto_send_em.sendInfo(md5 + "\n" + Latest_Event)
        # file.write(md5 + Latest_Event + "Time of LA" + time.ctime() + "\n" )
        # file.close()
    else:
        auto_send_em.sendInfo("Nothing Changed \n\n" + "MD5 Check \n" + md5 + "\n" + "The Latest Event is \n" + Latest_Event)
        # file.write("md5 and Latest_Event Didn't Change on Time of LA" + time.ctime() + "\n" )
        # file.close()
    
    return 