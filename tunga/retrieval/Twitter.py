import tweepy as tw

auth = tw.OAuthHandler('imW937M6khWYK3utt6rgUNwC9', 'NHrbDvcnvoqOIJjWKhUXZPAfsToM3k9X8mQoslGF0w24xiJknR')
auth.set_access_token('246202949-DZ5kRviZM7cBJFyp1gMZw3GytoIsbGMBhNt3pGOW',
                      'n7G3SblCHd9URjIAugRRBZKqYLUVyDYtf39vuYvgaqE9q')
api = tw.API(auth)


def read_tweets_from_user(username, max_tweet_count):
    user = api.user_timeline(username, count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append({
            "tweet_text":tweet.text
        })
    return user_tweet


def read_tweets_from_hashtag(hashtag, date, max_tweet_count):
    search_words = hashtag + "-filter:retweets"
    date_since = date

    tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang="tr",
                       since=date_since).items(max_tweet_count)
    date_tweet = []
    for tweet in tweets:
        date_tweet.append(tweet.text)
    return date_tweet


def read_tweets_from_mention(max_tweet_count):
    user = api.mentions_timeline(count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append(tweet.text)

    return user_tweet
print(read_tweets_from_mention(20))
