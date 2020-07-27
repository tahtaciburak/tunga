import tweepy as tw


def read_tweets_from_user(api_key, api_secret, access_token, token_secret, username, max_tweet_count):
    auth = tw.OAuthHandler(api_key, api_secret, )
    auth.set_access_token(access_token, token_secret)
    api = tw.API(auth)
    user = api.user_timeline(username, count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append({
            "tweet_text": tweet.text
        })
    return user_tweet


def read_tweets_from_hashtag(api_key, api_secret, access_token, token_secret, hashtag, date, max_tweet_count):
    auth = tw.OAuthHandler(api_key, api_secret, )
    auth.set_access_token(access_token, token_secret)
    api = tw.API(auth)
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


def read_tweets_from_mention(api_key, api_secret, access_token, token_secret, max_tweet_count):
    auth = tw.OAuthHandler(api_key, api_secret, )
    auth.set_access_token(access_token, token_secret)
    api = tw.API(auth)

    user = api.mentions_timeline(count=max_tweet_count)

    user_tweet = []
    for tweet in user:
        user_tweet.append({
            "tweet_text": tweet.text
        })

    return user_tweet
