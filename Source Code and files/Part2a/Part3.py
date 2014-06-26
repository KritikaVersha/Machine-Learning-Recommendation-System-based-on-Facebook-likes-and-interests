import sqlite3 as sqlite
import re
import operator
import cmd

class SimilarLikes(cmd.Cmd):
    
   
########## Function to end the program    
    def do_EOF(self, line):
        return True

########## Function to recommend like and interest pages
    def do_recommend(self,line):
        
########## Function REGEX to do pattern matching for variables as well as sqlite tables
        def REGEXP(expr, item):
            item=item.replace('[','').replace(']','')
            r = re.compile(expr,re.UNICODE)
            return r.match(item) is not None
        
########## This part of the code is used to fetch results from the SQL Table 'similar'.The results are based on 
########## most commonly observed likes which occur together for the user list.The file is extracted from question 2
        with sqlite.connect(r'Scopely.db') as con: 
          d={}
          cur = con.cursor()
          con.create_function("REGEXP", 2, REGEXP)
          testVar1 = raw_input("Enter your likes and interests")
          user_id = raw_input("Enter your user id")
          testVar=testVar1.replace(",","|")
          cur.execute("Select Like,Frequency from similar WHERE LIKE REGEXP ? ORDER BY Frequency DESC",(testVar,),)    
          rows=cur.fetchall()
          for i in rows:        
              key=list(i)[0].replace(testVar1,"").strip()
              value=list(i)[1]
              if key in d:
                d[key]+=value
              else:
                d[key]=value
                
                
########## This part of the code removes the recommended likes from the list which are already present for the given user id
          user_like=[]
          cur.execute("Select LIKES from likes WHERE ID LIKE ?", (user_id,))
          row_id=cur.fetchall()
          for i in row_id:
             for j in i:
                  k=j.encode('utf-8').replace('[','').replace(']','').replace('\\n','').replace(" ","")
                  user_like=k.split(',') 
          for i in d.keys():
            if i in user_like:
              del d[i]
              
########## Displaying the results               
        for k,v in reversed(sorted(d.items(),key=operator.itemgetter(1))):
            print k,v
        
        
if __name__ == '__main__':
    SimilarLikes().cmdloop()
     
     
