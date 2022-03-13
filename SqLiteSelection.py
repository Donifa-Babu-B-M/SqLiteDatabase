#!/usr/bin/python

#To Select the data from SqLite Database - Movie Table
import sqlite3

conn = sqlite3.connect('Movies.db')
print("Lets display the movie table from the database!")
print("Opened database successfully")

cursor = conn.execute("SELECT * from MOVIE")
for row in cursor:
   print("ID            = ", row[0])
   print("NAME          = ", row[1])
   print("ACTOR         = ", row[2])
   print ("ACTRESS       = ", row[3])
   print("DIRECTOR      = ", row[4])
   print("YEAR          = ", row[5])
   print("********************************")

print("Selection done successfully");
conn.close()