import sqlite3 as sqlite
import re
import operator
import cmd,sys

class SimilarUser(cmd.Cmd):

    
########## Function to end the program     
    def do_EOF(self, line):
        return True


########## Function to recommend similar users    
    def do_user(self,line):
        
########## Function REGEX to do pattern matching for variables as well as sqlite tables
        def REGEXP(expr, item):
            item=item.replace('[','').replace(']','')
            r = re.compile(expr,re.UNICODE)
            return r.match(item) is not None
            
        
########## This part of the code is used to fetch results from the SQL Table 'likes'.The results are based on 
########## most commonly observed likes which occur together for the user list.The file is extracted from question 2        
        with sqlite.connect(r'Scopely.db') as con: 
          cur = con.cursor()
          con.create_function("REGEXP", 2, REGEXP)
          testVar1 = raw_input("Enter your likes and interests")
          userID = raw_input("Enter your user id")
          testVar=testVar1.replace(",","|")
          cur.execute("Select * from likes WHERE LIKES REGEXP ? AND ID NOT LIKE ?", (testVar,userID),)
          rows=cur.fetchall()

########## Adding the fetched results to  the dictionary
          d={}
          for i in rows:
             for j in i:
                  k=j.encode('utf-8').replace('[','').replace(']','').replace('\\n','')
                  match = re.findall(testVar, k)
                  if len(match)>0:
                    key=str(list(i)[0])+str(match)
                    d[key]=len(match)

########## Displaying the results
          for k,v in reversed(sorted(d.items(),key=operator.itemgetter(1))):
              sys.stdout.write(k+'\t'+str(v)+'\n')

if __name__ == '__main__':
    SimilarUser().cmdloop()
     
     
