import json

import pymongo
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["20200315"]
tweets_coll = db["tweets"]

consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""


class listener(StreamListener):
    count = 0

    def on_data(self, data):
        tweets_coll.insert_one(json.loads(data))
        self.count += 1
        print(self.count)
        return (True)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=[
    "#Dia15PeloBrasil", "Dia15BrasilNasRuas", "15DeMarcoEuVou",
    "Dia15PorBolsonaro", "BolsonaroDay"
])
