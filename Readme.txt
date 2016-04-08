These instructions assume that postgres, python 2.7, and streamparse are already installed.

Instructions:

	1) If the Tcount database has not already been created:
		-su - postgres
		-Create database Tcount;
		-exit;
	2) Clone my repo into your local directory
	3) cd ~/TwitterStormApp
	4) python makePostgres.py
	5) To run the application:
		-cd ex2tweetwordcount
		-sparse run
	6) To run serving scripts
		-cd ~/TwitterStormApp
		-python finalresults.py <optional_word_argument>
		-python histogram.py <k1_argument> <k2_argument>