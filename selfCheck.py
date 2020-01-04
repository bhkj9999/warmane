import warmane_notification
import auto_send_em
from resources import url
from Receiver import receiver


def selfCheck():
    
    md5 = warmane_notification.md5(url)
    Latest_Event_List = warmane_notification.getAllPelement(url)
    Latest_Event = Latest_Event_List[0] if Latest_Event_List else 'Error'


    auto_send_em.sendInfo("Email Function Works Fine \n\n" + "MD5 Check \n" + md5 + "\n\n" + "The Latest Event is \n" + Latest_Event, receiver[0])


selfCheck()