import numpy as np
import pandas as pd
import os
import tweepy as tw
import yaml
import lxml

# Twitter API Crendentials

consumer_key = "Ganmnp3P1N5vFHZSiSwQf53IN"
consumer_secret = "4U0YLsgsY1paRnwJYHum4WISEN01qN3zr4iS7kw3RvY6ye4Dij"
access_token = "1519783902604365824-7Yuy108u7v0BrNuIVFRlvoEiAQSW8h"
access_token_secret = "********************************************"

# Authenticate
auth = tw.OAuthHandler(consumer_key, consumer_secret)
# Set Tokens
auth.set_access_token(access_token, access_token_secret)
# Instantiate API
api = tw.API(auth, wait_on_rate_limit=True)

hashtag = "#ukraine"
query = tw.Cursor(api.search_tweets, lang="en", q=hashtag).items(1000)
posts = [{'Tweet':tweet.text} for tweet in query]

# Create a dataframe with a column called tweets

df = pd.DataFrame( [tweet['Tweet'] for tweet in posts] , columns=['Tweets'])


data_path = os.path.join("data")

data_extracted_path = os.path.join(data_path, "UkraineData.csv")

df.to_csv(data_extracted_path)

