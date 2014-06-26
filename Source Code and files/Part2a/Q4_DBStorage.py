import sqlite3 as sqlite

list2=[]
with sqlite.connect(r'Recommendations.db') as con: 
  cur = con.cursor()
  #cur.execute("DROP TABLE likes")
  cur.execute("CREATE TABLE IF NOT EXISTS likes(ID integer, LIKES text)") 
  
  with open('C:\\Users\\Kri89\\Desktop\\HighFreqUserLikes.csv') as file1:
        print "File Open"
        for i in file1.readlines():
            i=i.replace('\"','').replace('\'','')
            list1=i.split(',')
            list2.append([str(list1[0]),str(list1[1:])])

  cur.executemany("INSERT INTO likes VALUES (?,?)", list2)
  con.commit()
  cur.execute('UPDATE LIKES SET ID= REPLACE(ID,"\'","") ')
  cur.execute("UPDATE LIKES SET ID= REPLACE(ID,'\"','') ")
  cur.execute('UPDATE LIKES SET likes= REPLACE(likes,"\'","") ')
  cur.execute("UPDATE LIKES SET likes= REPLACE(likes,'\"','') ")
 

with sqlite.connect(r'Scopely.db') as con: 
  cur = con.cursor()
  #cur.execute("DROP TABLE similar")  
  cur.execute("CREATE TABLE IF NOT EXISTS similar(Like text, Frequency integer)") 
# 
#  
  list4=[] 
  with open('C:\\Users\\Kri89\\Desktop\\High__Freq_Like_Pairs.csv') as file1:
        print "File Open"
        for i in file1.readlines():
            i=i.replace('\"','').replace('\'','').replace('(','').replace(')','').replace('\n','')
            list3=i.split(',')
            list4.append([str(list3[0]).strip(),list3[1]])
  #print list4

  cur.executemany("INSERT INTO similar VALUES (?,?)", list4)
  cur.execute("SELECT * FROM similar")
  con.commit()
  rows=cur.fetchall()
  
  
