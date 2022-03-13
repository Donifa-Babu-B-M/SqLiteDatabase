#!/usr/bin/python

#To Select the data from SqLite Database - Movie Table
import sqlite3

conn = sqlite3.connect('Movies.db')
print("Lets make a selection with conditions/parameters")
print("Opened database successfully")
#Given a condition such as to display movies and cast in the year 2022
cursor = conn.execute("SELECT NAME,ACTOR,ACTRESS from MOVIE where YEAR=2022")
for row in cursor:

   print("NAME          = ", row[0])
   print("ACTOR         = ", row[1])
   print("ACTRESS       = ", row[2])

   print("********************************")

print("Selection With parameter (Movies released in the Year 2022) done successfully");
conn.close()