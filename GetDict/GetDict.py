#/usr/bin/env python
#-*-coding:utf-8-*-
#-*-encoding=utf-8
 
import urllib.request
from bs4 import BeautifulSoup
import codecs
import time
import sys

def get_defination(word):
    url="http://dict.baidu.com/s?device=mobile&wd=" + word.strip().replace(' ', '+')

    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'
        }
    )

    try:
        response = urllib.request.urlopen(req)
        html = response.read()
    except Exception as e:
        print(e)
        return None

    soup = BeautifulSoup(html,'html.parser')


    div = soup.find(id='simple_means-wrapper')
    if div == None:
        response.close()
        return div
    p_list = [p.get_text() for p in div.find_all('div')[1].find_all('p')]
    #print(uhtml.encode('GB18030'))
    response.close()
    return (' ').join(p_list)


# Script starts from here
if len(sys.argv) < 2:
    print('Usage: GetDict.py source_word_list.txt target_output_file.txt')
    sys.exit()


# open word list
input_file = open(sys.argv[1], 'rU')

# open output file
output_file = codecs.open(sys.argv[2],"w","utf-8")

# get word's defination and write to file
for word in input_file:

    if word.strip() == '':
        continue
    while True:
        definations = get_defination(word.strip())
        if definations != None:
            break
        print('Retry..................................', end='')
        print(word)
    
    line = word.strip() + '\t' + definations
    print(line)
    print(line, file=output_file)
    #time.sleep(1)

input_file.close()
output_file.close()
