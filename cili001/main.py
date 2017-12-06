# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re
import codecs

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf-8'
        print(r.encoding)

        return r.text
    except:
        return ""

def getindexInfo(indexURL,fpath):
    count = 0
    html = getHTMLText(indexURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('dd')
    # 打开文件
    fo = codecs.open("test.txt", "w", "utf-8")
    for i in a:
        try:
            magnet = i.attrs['magnet']
            ed2k = i.attrs['ed2k']
            t=i.a.string
            fo.write( t )
            fo.write( "\n" )
            fo.write( magnet )
            fo.write( "\n" )
            fo.write( ed2k )
            fo.write( "\n" )
            count = count + 1
            print("\rNo:",count)
        except:
            count = count + 1
            print("Error No:",count)
        continue
    # 关闭文件
    fo.close()

def main():
    index_info_url = 'http://oabt001.com/'
    output_file = './test.txt'
    getindexInfo(index_info_url, output_file)

main()
