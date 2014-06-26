#!/usr/bin/env python

import string
import matplotlib.pyplot as plt
import numpy as np

file1 =open('C:\\Users\\Kri89\\Desktop\\reduced1.csv', 'r')
likes={}
xplot=[]
yplot=[]
alnum = set(string.letters + string.digits)
for i in file1.readlines():
    list1= i.replace("\n","").split(",")
    list1.remove(list1[0])
    for j in list1:
        if(j in likes):
            likes[j] += 1
        else:
            likes[j] = 1

for k,v in likes.items():
     k=filter(lambda x: x in string.printable, k)
     if (len(set(k) & alnum) > 0) and (v>1500) : 
       xplot.append(k)
       yplot.append(v) 

print "Number of likes and interests "+str(len(yplot))
#print "Maximum of the frequency count "+str(max(yplot))
#a=np.array(yplot)
#print "Mean of the frequency count "+str(np.mean(a))
#print "2.5th percentile of the frequency count "+str(np.percentile(a,2.5))
#print "25th percentile of the frequency count "+str(np.percentile(a,25))
#print "50th percentile of the frequency count "+str(np.percentile(a,50))
#print "75th percentile of the frequency count "+str(np.percentile(a,75))
#print "90th percentile of the frequency count "+str(np.percentile(a,90))
#print "95th percentile of the frequency count "+str(np.percentile(a,95))
#print "97.5th percentile of the frequency count "+str(np.percentile(a,97.5))
#print "99.5th percentile of the frequency count "+str(np.percentile(a,99.5))
#print "Standard Deviation "+str(np.std(a,axis=0))
hist, bin_edges = np.histogram(yplot, bins = 100)
plt.bar(bin_edges[:-1], hist, width = 1)
plt.xlim(min(bin_edges), max(bin_edges))
plt.show()  
