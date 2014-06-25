import pydot
from bs4 import BeautifulSoup
import json, urllib2, urllib
import itertools 

write_step2 =open('C:\Users\Kri89\Desktop\Proj5_File.txt', 'w')
response = urllib2.urlopen('http://www.rasnz.org.nz/Stars/Constellations.shtml#months')
f = urllib.urlretrieve('http://www.rasnz.org.nz/Stars/Constellations.shtml#months', 'C:/Users/Kri89/Desktop/Pro_step2.html')
html_doc=response.read()
write_step2=open('C:\Users\Kri89\Desktop\Proj5_File.txt', 'w')
file = open("C:/Users/Kri89/Desktop/Pro_step2.html","wb") #open file in binary mode
file.writelines(html_doc)
file.close()
db1=[]
soup=BeautifulSoup(html_doc)
constellation_table = soup.find_all('table')[0]
#print constellation_table
count=0
for i in constellation_table.find_all('table')[1]:
    soup1=BeautifulSoup(str(i))
    for j in soup1.find_all('td'):
        #print j
        if 'palegreybold' in str(j):
            count=count+1
            write_step2.write("\n"+str(count)+"\t"+j.text)
            write_step2.write("\t")
        else:
            write_step2.write(","+j.text.encode('utf-8'))
        
            
            