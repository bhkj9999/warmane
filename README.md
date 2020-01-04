# ***warmane Event Tracking***
 
## Project Target
### Send Request To Waramene Website To Get the latest Event, and send the Event Title & HTML link to your Email Address
---
## How To Process
### the Request and Parse Process
#### in warmane_notification.py

#### Get All ```<p>```Element and append them into a list, convert the list to string, and use hashlib to get the md5 value, so we can know the warmane event has changed through the change of value of this md5.
---
## what you need to Do
1. Because the email service I used is Gmail, if you need other smtp service provider you need to change some code of auto_send_em.py.
2. Create a python file and add your account name and your password.
3. Create a receiver list to set the Email Receiver.