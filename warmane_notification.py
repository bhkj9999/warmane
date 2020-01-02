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
            result.append(str(i))

    return result

def printElement():
    final = getAllPelement()

    print(final)

    return final

def md5():
    final = getAllPelement()

    md5 = hashlib.md5()

    md5.update(str(final).encode('utf-8'))

    print(md5.hexdigest())

    return md5.hexdigest()