#!/usr/bin/python

#To Select the data from SqLite Database - Movie Table
import sqlite3

conn = sqlite3.connect('Movies.db')
print("Lets display the details of movie based on actor name")
print("Opened database successfully")
#Given a condition such as to display details of movie based on actor name
cursor = conn.execute("SELECT * from MOVIE where ACTOR='Dulquer Salmaan'")
for row in cursor:
   print("ID             = ", row[0])
   print("NAME          = ", row[1])
   print("ACTOR         = ", row[2])
   print("ACTRESS       = ", row[3])
   print("DIRECTOR      = ", row[4])
   print("YEAR          = ", row[5])

print("********************************")

print("Selection Based on ACTOR name done successfully");
conn.close()