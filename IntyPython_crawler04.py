from bs4 import BeautifulSoup
import requests

baidu=requests.get('https://www.baidu.com').content
soup=BeautifulSoup(baidu,'html.parser')
LinkWords=soup.findAll('a')

for linkword in LinkWords:
    print(linkword)