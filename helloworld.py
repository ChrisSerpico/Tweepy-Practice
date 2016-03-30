# helloworld.py
# Tweets from text file 

# imports
import tweepy, time, sys

# get file from first argument
argfile = str(sys.argv[1])

# info from twitter application 
# this is read from file 'secrets.txt'
secretfile = open('secrets.txt', 'r')
s = secretfile.read().splitlines()
secretfile.close()

CONSUMER_KEY = s[0]
CONSUMER_SECRET = s[1]
ACCESS_KEY = s[2]
ACCESS_SECRET = s[3]

# authenticate
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# read tweets from file
filename = open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(status=line)
	time.sleep(60) # tweet every minute 
