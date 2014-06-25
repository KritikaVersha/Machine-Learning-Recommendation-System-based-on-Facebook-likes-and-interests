# -*- coding: utf-8 -*-      
import urllib2, json, csv,requests,re
from time import sleep
import sqlite3 as sqlite

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
  cur.execute("ALTER TABLE light ADD COLUMN Year integer;")
  cur.execute("UPDATE light SET year=substr(obsvdate,-4) ")  
  #Misprint in 2013 database.2013 labelled as 2003
  cur.execute("UPDATE light SET year=2013 WHERE year=2003") 
  
  ############Below commands are used after adding year column in the light column
  ############Formatting the months in light table. 
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-January') WHERE obsvdate LIKE '1/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-February') WHERE obsvdate LIKE '2/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-March') WHERE obsvdate LIKE '3/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-April') WHERE obsvdate LIKE '4/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-May') WHERE obsvdate LIKE '5/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-June') WHERE obsvdate LIKE '6/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-July') WHERE obsvdate LIKE '7/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-August') WHERE obsvdate LIKE '8/%'")
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-September') WHERE obsvdate LIKE '9/%'")  
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-October') WHERE obsvdate LIKE '10/%'")  
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-November') WHERE obsvdate LIKE '11/%'")  
  cur.execute("UPDATE light SET obsvdate=(obsvdate || '-December') WHERE obsvdate LIKE '12/%'") 
  rows = cur.fetchall()
  print rows
  #check_result(str(cur.fetchone()[0]), "9")
  