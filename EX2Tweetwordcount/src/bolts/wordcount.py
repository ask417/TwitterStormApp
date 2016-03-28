from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
#import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        self.redis = StrictRedis()
	#self.conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")

    def process(self, tup):
        word = tup.values[0]

	# Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
	#cur = self.conn.cursor()
	#cur.execute("select * from tweetwordcount where word=%s", (word))
	#record = cur.fetchall()

	#if len(record)==0:
	#	cur.execute("insert into tweetwordcount (word,count) values (%s, 1)",(word))
	#else:
	#	cur.execute("update tweetwordcount set count=%s where word=%s",(count,word))

	#self.conn.commit()
	#self.conn.close()
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
