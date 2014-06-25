#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pydot
from bs4 import BeautifulSoup
import json, urllib2, urllib
import itertools 

write_step4 =open('C:\Users\Kri89\Desktop\step4.txt', 'w')
write_step2 =open('C:\Users\Kri89\Desktop\step2.txt', 'w')
response = urllib2.urlopen('http://www.imdb.com/search/title?at=0&sort=num_votes&count=100')
f = urllib.urlretrieve('http://www.imdb.com/search/title?at=0&sort=num_votes&count=100', 'C:/Users/Kri89/Desktop/step1.html')
html_doc=response.read()
file = open("C:/Users/Kri89/Desktop/step1.html","wb") #open file in binary mode
file.writelines(html_doc)
file.close()
count=0
soup=BeautifulSoup(html_doc)
movie_table = soup.find_all('table')[0]
title=[]
Actors_Only=set()
Actor_Set=[]
for row in movie_table.find_all('td',{ "class" : "image" }):
  count=count+1
  number=str(count)
  row1=str(row)
  soup1=BeautifulSoup(row1)
  for a in soup1.find_all('a', href=True):
    titlestep1=(a['href'].strip('/')).encode()
    write_step2.write(titlestep1[6:].encode()+'\t'+number+'\t'+a['title'].encode('utf-8')+"\n")
    title.append(str(a['href'].strip('/')[6:]))
with open("C:/Users/Kri89/Desktop/step3.txt","w") as file1: #open file in binary mode
    #print(title)
    for i in title:
        responsejson = urllib2.urlopen("http://www.omdbapi.com/?i="+i)
        text = str(responsejson.read())
        text=text.replace("}","}"+"\n")

        responsejson.close()
        #print(text)
        file1.writelines(text)
file1.close()

with open("C:\Users\Kri89\Desktop\step3.txt",'rU') as f:
    for line in f:
       
        json_str=json.loads(line) 
        Movie_Title=json_str.get('Title').encode('utf-8') 
        Actors=json_str.get('Actors') 
        First_Four_Actors=Actors.split(',')
        perm=itertools.combinations(First_Four_Actors,2)
        for i in perm:
            #print (i)
            Actor_Set.append(i)

        write_step4.write(Movie_Title+'\t[\"'+First_Four_Actors[0].encode('utf-8')+'\",\t'+First_Four_Actors[1].encode('utf-8')+'\",\t\"'+First_Four_Actors[2].encode('utf-8')+'\",\t\"'+First_Four_Actors[3].encode('utf-8')+'\"]')
        
    graph = pydot.Dot(graph_type='graph',charset="utf8")
    
    for i in list(Actor_Set):
        klm= list(i)
        graph.add_edge(pydot.Edge(klm[0],klm[1]))

    graph.write('C:\Users\Kri89\Desktop\\actors_graph_output.dot')
