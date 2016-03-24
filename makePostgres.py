import psycopg2

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query,
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows.

#cur = conn.cursor()

