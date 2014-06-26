import nltk
import  csv
import string

file1 =open('C:\\Users\\Kri89\\Desktop\\Cleanedup_File.csv', 'r')
file2 =open('C:\\Users\\Kri89\\Desktop\\HighFrequencyLike_1235_File.csv', 'wb')
csv_write=csv.writer(file2,delimiter=',')
file4 =open('C:\\Users\\Kri89\\Desktop\\HighFreqUserLikes.csv', 'wb')
csv_wrote=csv.writer(file4,delimiter=',')
file3 =open('C:\\Users\\Kri89\\Desktop\\Cleanedup_File.csv', 'r')
csv_write=csv.writer(file2,delimiter=',')
likes={}
xplot=[]

alnum = set(string.letters + string.digits)
for i in file1.readlines():
    list1= i.replace("\n","").split(",")
    list1.remove(list1[0])
    for j in list1:
        if(j in likes):
            likes[j] += 1
        else:
            likes[j] = 1
file1.close()
print"Counting high freq likes"
for k,v in likes.items():
     k=filter(lambda x: x in string.printable, k)
     k=k.replace("\"","").replace(" ","")
     if (len(set(k) & alnum) > 0) and (v>=1235) : 
       xplot.append(k)

d={}
for i in file3.readlines():
    user_id=i.split(':')[0]
    token1=nltk.tokenize.RegexpTokenizer(r'\w+').tokenize(i)
    token= sorted(list(set(token1).intersection(set(xplot))))
    csv_wrote.writerow([str(user_id),str(token)])
    if len(token)>0:
        pairs=nltk.bigrams(token)
    #print pairs
        bigram_measures=nltk.collocations.BigramAssocMeasures()
        finder=nltk.collocations.BigramCollocationFinder.from_words(pairs)
        for i in pairs:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print len(d)

for k,v in d.items():
    csv_write.writerow([str(k),str(v)])

