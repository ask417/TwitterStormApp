import sys, re, psycopg2

try:
	if not (len(sys.argv) == 3 and isinstance( int(sys.argv[1]), ( int, long ) ) and isinstance( int(sys.argv[2]), ( int, long ) )):
		print("Invalid or missing arguments")
		exit()
except ValueError:
	print("Non-integers passed, please stop doing that")
	exit()

sys.argv[1] = int(sys.argv[1])
sys.argv[2] = int(sys.argv[2])

conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("select * from tweetwordcount where count>={0} and count<={1}".format(sys.argv[1],sys.argv[2]))
rec = cur.fetchall()
rec = sorted(rec, key=lambda x: x[0])

for pair in rec:
	print(pair[0]+": "+str(pair[1]))

conn.commit()
conn.close()

