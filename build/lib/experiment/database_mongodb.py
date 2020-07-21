import pymongo
from tunga.retrieval import Twitter

tungaclient = pymongo.MongoClient("mongodb://localhost:27017/")

tungadb = tungaclient["tungadatabase"]

#print(tungaclient.list_database_names())

mycol = tungadb["tweets"]
print(tungadb.list_collection_names())

hashtag_tweet= Twitter.read_tweets_from_hashtag("#hasta", "2020-04-05", 10)
hashtag_tweet2= Twitter.read_tweets_from_hashtag("#hastalık", "2020", 20)

database = mycol.insert_many(hashtag_tweet)

print(database.inserted_ids)
myresult = mycol.find().limit(15)
data = mycol.insert_many(hashtag_tweet)
for data in myresult:
    print(data)
