"""
    Module that takes care of interaction with twitter APIs
"""

import json
import os
import tweepy

from app_config import app_config


class TwitterConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.auth = None

    def __authenticate(self):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
        auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
        return auth

    def __get_home_timeline(self, params=None):
        if not params:
            params = {}
        auth = self.__authenticate()
        # Create API object
        api = tweepy.API(auth)
        # Get the timeline of tweets
        params = dict(count=params.get('count', 200), since_id=params.get('last_synced_tweet_id', 0),
                      exclude_replies=True)
        timeline = api.home_timeline(**params)

    def get_timeline(self, params=None):
        # Returning data from mock for now
        with open('app_config/mock_timeline.json') as config_file:
            return json.load(config_file)
        # TODO Connect to twitter API using developer account and get timeline of tweets
        # timeline = self.__get_home_timeline(params)
        # tweet_list = [vars(tweet) for tweet in timeline]
        # return tweet_list
