#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pydot
from bs4 import BeautifulSoup
import json, urllib2, urllib
import itertools 

write_step2 =open('C:\Users\Kri89\Desktop\Proj2_File.txt', 'w')
response = urllib2.urlopen('http://www.nightskyatlas.com/constellations.jsp')
f = urllib.urlretrieve('http://www.nightskyatlas.com/constellations.jsp', 'C:/Users/Kri89/Desktop/Pro_step1.html')
html_doc=response.read()
file = open("C:/Users/Kri89/Desktop/Pro_step1.html","wb") #open file in binary mode
file.writelines(html_doc)
file.close()
db1=[]
soup=BeautifulSoup(html_doc)
constellation_table = soup.find_all('table')[5]
data=[row.string.encode('utf-8')+"\t" for row in constellation_table.find_all('td',{ "class" : "data" })]
chunks=[data[x:x+11] for x in xrange(0, len(data), 11)]
for i in chunks:
        write_step2.writelines(i)
        write_step2.write("\n")



        
    

  