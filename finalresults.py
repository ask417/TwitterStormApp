import sys, re, psycopg2

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()

if len(sys.argv)>1:
	cur.execute("select * from tweetwordcount where word='{0}'".format(sys.argv[1]))
else:
	cur.execute("select * from tweetwordcount")

rec = cur.fetchall()
rec = sorted(rec, key=lambda x: x[0])

for pair in rec:
	print(pair)

conn.commit()
conn.close()

