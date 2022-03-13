#!/usr/bin/python

#To insert data into Sqlite database - Movie Table
import sqlite3

conn = sqlite3.connect('Movies.db')
print("Opened database successfully");

conn.execute("INSERT INTO MOVIE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (1, 'Radhe Shyam', 'Prabhas', 'Pooja Hedge', 'Radha Krishna Kumar', 2022 )");

conn.execute("INSERT INTO MOVIE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (2, 'The Batman', 'Robert Pattinson', 'Zoe Kravitz', 'Matt Reeves', 2022 )");

conn.execute("INSERT INTO MOVIE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (3, 'Hey Sinamika', 'Dulquer Salmaan', 'Aditi Rao Hydari', 'Brinda', 2022 )");

conn.execute("INSERT INTO MOVIE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (4, 'Kutty', 'Dhanush', 'Shriya Saran', 'M.Jawahar', 2010 )");

conn.execute("INSERT INTO MOVIE (ID,NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) \
      VALUES (5, 'Enthiran', 'Rajinikanth', 'Aishwarya Rai', 'S.Shankar', 2010 )");


conn.commit()
print("Records inserted successfully");
conn.close()