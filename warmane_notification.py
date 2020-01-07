'''
@Author: Henry Zhang
@Github: https://github.com/bhkj9999
@Date: 2020-01-01 21:09:04
@LastEditTime : 2020-01-06 11:39:09
@LastEditors  : Henry Zhang
@Description: Retrive the event information and notify
@FilePath: /warmane/warmane_notification.py
'''

import requests
from bs4 import BeautifulSoup
import hashlib

def getFormattedRes(url):
    res = requests.get(url)

    resCode = res.status_code
    
    formattedRes = BeautifulSoup(res.text, 'html.parser')

    return formattedRes, resCode

def getAllPelement(url):
    text = getFormattedRes(url)[0] if getFormattedRes(url)[0] else 'Error'

    all_P_Tag = text.findAll('p')

    filter_A = 'href'

    result = []

    for i in all_P_Tag:
        if(filter_A in str(i)):
            processedString = str(i).replace('<p>', '').replace('<a href="', 'at ').replace('">here</a>.</p>', '').replace('<!--StartFragment-->', '').replace('">here</a>.<!--EndFragment--></p>', '')
            # processedString = processedString + 'TryError'
            result.append(processedString)

    return result

def printElement(url):
    final = getAllPelement(url)
    
    for i in final:
        print (i + "\n")

    return

def md5(url):
    final = getAllPelement(url)

    md5 = hashlib.md5()

    md5.update(str(final).encode('utf-8'))

    return md5.hexdigest()