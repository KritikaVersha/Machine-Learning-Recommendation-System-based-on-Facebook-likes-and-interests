import string
import csv


def main():
   file1 =open('C:\\Users\\Kri89\\Desktop\\likes.csv', 'r')
   with open('C:\\Users\\Kri89\\Desktop\\Cleanedup_File.csv','wb') as file3:
    csv_write=csv.writer(file3,delimiter=',')
    print "Counting the like pages on facebook"
    alnum = set(string.letters + string.digits)
    
    count=0
    for i in list(file1):
       i=filter(lambda x: x in string.printable, i)
       i=' '.join(i.split())
       i=i.replace(", "," ").replace(" ,"," ")
       list1= i.split(',')
       list1=filter(lambda k: (len(k)>4 and len(set(k) & alnum) > 0), list1)
       if len(list1) >=2:
           count=count+1
           list1[0]=str(list1[0]+':')
           csv_write.writerow(list1)
    print "Number of user records: "+str(count)

    
if __name__ == '__main__':
  main()
      
