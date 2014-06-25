import urllib2, json, csv,requests,re
from time import sleep
import sqlite3 as sqlite


csv_out_profile = csv.writer(open('C:\Users\Kri89\Desktop\\final_report_kmversha.csv', 'wb'), delimiter=',')
#################################################################
##   Creating a database
#################################################################


def check_result(result, desired):
  if result != desired:
    print "NOT_OK.  Expected " + desired + "; but got "+result
  else:
    print "OK!"
  return


with sqlite.connect(r'si-601-project_kmversha.db') as con:
  con.text_factory = str 
  cur = con.cursor()
  
  ########### Calculating limiting magnitude with  combined tables comparing it with months
  print "\n Calculating limiting magnitude with  combined tables comparing it with months"
  row1=cur.execute("SELECT light.constellation,light.year,visibility_months.month,avg(light.magnitude),constellation.p_star,constellation.visibility from light join visibility_months join constellation WHERE (light.magnitude<=7.0 and light.magnitude>0) and light.obsvdate LIKE ('%'||visibility_months.month) and visibility_months.visible_const LIKE ('%'||light.constellation||'%') and constellation.latin_name=light.constellation and light.constellation IS NOT NULL GROUP BY light.constellation,substr(light.obsvdate,0,2),light.year ORDER BY light.year")
  for i in row1:
    print i
    
  ########### Calculating limiting magnitude with  table light comparing it with months
  print "\n Calculating limiting magnitude with  table light comparing it with months"
  row2=cur.execute("SELECT light.year,substr(obsvdate,10),avg(light.magnitude) from light WHERE (light.magnitude<=7.0 and light.magnitude>0) and light.constellation IS NOT NULL and light.year>=2010 and light.year<=2013 GROUP BY substr(light.obsvdate,0,2),light.year ORDER BY light.year") 
  for i in row2:
    print i
    
  ########### Calculating limiting magnitude with combining both the tables comparing it with months
  print "\n Calculating limiting magnitude with combining both the tables comparing it with months"
  row3=cur.execute("SELECT light.year,visibility_months.month,avg(light.magnitude) from light join visibility_months join constellation WHERE (light.magnitude<=7.0 and light.magnitude>0) and light.obsvdate LIKE ('%'||visibility_months.month) and visibility_months.visible_const LIKE ('%'||light.constellation||'%') and constellation.latin_name=light.constellation and light.constellation IS NOT NULL GROUP BY substr(light.obsvdate,0,2),light.year ORDER BY light.year")
  for i in row3:
    print i
    
  ########### Calculating yearly limiting magnitude with only using the table light
  print "\n Calculating yearly limiting magnitude with only using the table light"
  row4=cur.execute("SELECT light.year,avg(light.magnitude) from light WHERE (light.magnitude<=7.0 and light.magnitude>0) and light.year>=2010 and light.year<=2013 and light.constellation IS NOT NULL GROUP BY light.year ORDER BY light.year")
  for i in row4:
    print i
  
  #############Calculating yearly results using a combination of table
  print ("\n Calculating yearly results using a combination of table")
  row5=cur.execute("SELECT light.year,avg(light.magnitude) from light join visibility_months join constellation WHERE (light.magnitude<=7.0 and light.magnitude>0) and light.obsvdate LIKE ('%'||visibility_months.month) and visibility_months.visible_const LIKE ('%'||light.constellation||'%') and constellation.latin_name=light.constellation and light.constellation IS NOT NULL GROUP BY light.year ORDER BY light.year")
  for i in row5:
    print i
  
  ############# Finding the constellation- best visible month mismatch in the Globe At Night Dataset
  print("\n Finding the constellation- best visible month mismatch in the Globe At Night Dataset")
  row6=cur.execute("SELECT DISTINCT light.constellation,substr(light.obsvdate,10) from light join visibility_months where visibility_months.visible_const NOT LIKE ('%'||light.constellation||'%') and light.obsvdate LIKE ('%'||visibility_months.month)") 
  for i in row6:
    print i
    
  ############ Finding the best visibility period for Orion,Leo and crux
  print("\n Finding the best visibility period for Orion,Leo and Crux")
  row8=cur.execute("SELECT * FROM visibility_months where visible_const LIKE ('%'||'Orion'||'%') OR visible_const LIKE ('%'||'Leo'||'%') OR visible_const LIKE ('%'||'Crux'||'%') ") 
  for i in row8:
    print i
    
  ############ Finding the best visibility period for Orion,Leo and crux
  print("\n Finding the best visibility period for Orion,Leo and Crux")
  row7=cur.execute("SELECT * FROM visibility_months where month like 'March' or month like 'February' ") 
  for i in row7:
    print i
  #rows = cur.fetchall()
  #print rows
  #title=['Constellation','Year of Observation','Month of Observation','Light Magnitude','Number of Principal Stars','Best Visibility Month']
  #csv_out_profile.writerow(title)
  #for i in rows:
  #  #print i
  #  csv_out_profile.writerow(list(i))

  #check_result(str(cur.fetchone()[0]), "9")