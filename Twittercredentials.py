import tweepy

consumer_key = "W3GUkFIcRfvBF9cXPJrfVXS79"

consumer_secret = "KeYfwQBBS8yvegyNnfKMYirrD1ykybMAoCpj122v4I0cGSokGU";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "352916684-qetN4cNidtsIOb1jr1zJlVtX5EuMIQmCjOPokvKl";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "A5gVeVXldNlDWX5pOuqRKMWRfXX9GvJY6ycKXyGeHm3ur";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



