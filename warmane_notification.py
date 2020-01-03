'''
@Author: Henry Zhang
@Github: https://github.com/bhkj9999
@Date: 2020-01-01 21:09:04
@LastEditTime : 2020-01-02 11:34:10
@LastEditors  : Henry Zhang
@Description: Retrive the event information and notify
@FilePath: /warmane/warmane_notification.py
'''

import requests
from bs4 import BeautifulSoup
import hashlib

def getFormattedRes(url):
    res = requests.get(url)
    
    formattedRes = BeautifulSoup(res.text, 'html.parser')

    return formattedRes

def getAllPelement():
    url = 'https://www.warmane.com/'

    text = getFormattedRes(url)

    all_P_Tag = text.findAll('p')

    filter_A = 'href'

    result = []

    for i in all_P_Tag:
        if(filter_A in str(i)):
            processedString = str(i).replace('<p>', '').replace('<a href="', 'at ').replace('">here</a>.</p>', '').replace('<!--StartFragment-->', '').replace('">here</a>.<!--EndFragment--></p>', '')
            result.append(processedString)

    return result

def printElement():
    final = getAllPelement()
    
    for i in final:
        print (i + "\n")

    return

def md5():
    final = getAllPelement()

    md5 = hashlib.md5()

    md5.update(str(final).encode('utf-8'))

    print(md5.hexdigest())

    return md5.hexdigest()