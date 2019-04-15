import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib
import time
import re
import os

locations = [
    'https://www.python.org/'
]


try:
    for location in locations:
        html = requests.get(location)
        data = BeautifulSoup(html.content,'lxml')
        #print(data)
        file2 = open("Scrapped data/Whole data.txt","a+")
        file2.write(str(data))
        file2.close()
        for link in data.findAll('a', attrs={'href': re.compile("^http://")}):
            all_links = link.get('href')
            #print(all_links)
            file3 = open("Scrapped data/links.txt","a+")
            file3.write(all_links)
            file3.write("\n")
            file3.close()
            soup = BeautifulSoup(urlopen(all_links).read(),'html')

            title = (soup.title.string)
            #print(title)
            file1 = open("Scrapped data/title.txt","a+")
            file1.write(title)
            file1.write("\n")
            file1.close()
            
            for pp in soup.select("p"):
                pass
                para = pp.text
                #print (pp)
                file4 = open("Scrapped data/Paragraph.txt","a+")
                file4.write(str(para))
                file4.write("\n")
                file4.close()
            body = soup.body.text
            #print(body.text)
            file5 = open("Scrapped data/Body.txt","a+")
            file5.write(body)
            file5.write("\n")
            file5.close()
            head = soup.head.text
            #print(head.text)
            file5 = open("Scrapped data/Head.txt","a+")
            file5.write(head)
            file5.write("\n")
            file5.close()
            try:
                links = soup.find_all('img', src=True)
                for link in links:
                    timestamp = time.asctime() 
                    txt = open('web scraping images/%s.jpg' % timestamp, "wb")
                    link = link["src"].split("src=")[-1]
                    download_img = urlopen(link)
                    txt.write(download_img.read())

                    txt.close()
            except Exception as e:
                pass       
            
except Exception as e:
    print("\n"*20)
    print(e)
    pass