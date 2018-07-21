# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import time

def getURL(msg):
    r = requests.get('https://www.youtube.com/results?search_query=' + msg)

    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(r.text, 'html.parser')

    trueURL = ""
    for entry in soup.select('a'):
        m = re.search("v=(.*)", entry['href'])
        if m:
            trueURL = m.group(1)
            break
    if(trueURL !=""):
        trueURL = "https://www.youtube.com/watch?v=" + trueURL
    return trueURL

songName = "This is living"
print("如果getURL(songName) 回傳空字串，表示收尋不到")
print(getURL(songName))