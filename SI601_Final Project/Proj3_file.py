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
  #cur.execute("DROP TABLE light ")
  #cur.execute("CREATE TABLE light(obsvId text, latitude text, longitude integer,obsvdate text, obsvtime text, magnitude float,sqmread text, sqmserial text, cloud_cover text, constellation text, sky_comment text, location text, country text)")
  with open('C:\Users\Kri89\Desktop\Dataset\GaN2012.csv','r') as f1:
    db1=[]
    db2=[]
    for row in f1:
        row=row.split("\r")
        db1.extend(row)
    for i in db1:
        #For 2012 format
        #i=i.replace(",\n","")
        i=i.split(',')
        if len(i)==14:
            print i
            
        db2.append(i)
    cur.executemany("INSERT INTO light VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",db2)
  con.commit()
  cur.execute("SELECT COUNT(*) FROM light")
  
  #db3=[]
  #cur.execute("DROP TABLE constellation")
  #cur.execute("CREATE TABLE constellation(latin_name text, possessive text, abbrev text, eng_name text, visibility text, ra_hrs text, dec_degrees text, p_star integer, m_stars integer, ngc_obj integer, ic_obj integer)")
  #with open('C:\Users\Kri89\Desktop\Proj2_File.txt','r') as f2:
  #  for row in f2:
  #   row=row.replace("\t\n","")
  #   line1=row.split("\t")
  #   db3.append(line1)
  #cur.executemany("INSERT INTO constellation VALUES (?,?,?,?,?,?,?,?,?,?,?)", db3)
  #con.commit()
  ##cur.execute("SELECT * FROM constellation where visibility='January' or visibility='February' or visibility='March' or visibility='April'")
  #cur.execute("SELECT * FROM constellation ")
  #rows = cur.fetchall()
  #print rows
  ##check_result(str(cur.fetchone()[0]), "9")
  #
  #db4=[]
  #cur.execute("DROP TABLE visibility_months")
  #cur.execute("CREATE TABLE visibility_months (count integer, month text, visible_const text)")
  #with open('C:\Users\Kri89\Desktop\Proj5_File.txt','r') as f2:
  #  for row in f2:
  #   line1=row.split("\t")
  #   if len(line1)>1:
  #     db4.append(line1)
  #print db4
  #cur.executemany("INSERT INTO visibility_months VALUES (?,?,?)", db4)
  #con.commit()
  #
  
