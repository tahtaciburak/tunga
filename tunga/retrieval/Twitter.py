import tweepy as tw

api_key = 'imW937M6khWYK3utt6rgUNwC9'
api_secret = 'NHrbDvcnvoqOIJjWKhUXZPAfsToM3k9X8mQoslGF0w24xiJknR'
access_token = '246202949-DZ5kRviZM7cBJFyp1gMZw3GytoIsbGMBhNt3pGOW'
token_secret = 'n7G3SblCHd9URjIAugRRBZKqYLUVyDYtf39vuYvgaqE9q'

auth = tw.OAuthHandler(api_key, api_secret, )
auth.set_access_token(access_token, token_secret)
api = tw.API(auth)


def read_tweets_from_user(username, max_tweet_count):
    user = api.user_timeline(username, count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append({
            "tweet_text": tweet.text
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
        date_tweet.append({
            "tweet_text": tweet.text
        })
    return date_tweet


def read_tweets_from_mention(max_tweet_count):
    user = api.mentions_timeline(count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append({
            "tweet_text": tweet.text
        })

    return user_tweet
