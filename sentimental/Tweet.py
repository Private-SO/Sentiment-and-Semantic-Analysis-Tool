# Tweet.py used for data extraction from twitter.
import tweepy
import re

consumer_key = "XXX"
consumer_secret = "XXX"
access_token = "XXX-XXX"
access_token_secret = "XXX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)
file = open("tweettext.txt","w")

search_words = 'Canada OR University OR Dalhousie University OR Halifax OR Canada Education'


for tweet in tweepy.Cursor(api.search,
                               q=search_words,
                               lang="en").items(844):
  remove_specialchars = re.compile(r'http\S+|([^a-zA-Z\s]+?)|//?|<.*?>|\\|RT?')
  without_emojios = tweet._json["text"].encode('ascii', 'ignore').decode('ascii')
  json_str = remove_specialchars.sub(r'', without_emojios)
  file.write(json_str+"\n")

