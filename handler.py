"""
    Module that houses customized twitter functionalities
"""

import csv

from twitter_connector import TwitterConnector
from app_dao import AppDAO


class AppHandler:
    def __init__(self):
        pass

    def sync_tweets(self, request_data):
        """
            Method that takes care of syncing functionality by
            * Check if the user already exists in the system
            * Get authorization and save/update it
            * Get timeline data using Twitter API
            * Save it to the database
            * return list of available tweets for the user

        :return: List of tweets in the timeline
        :rtype: dict
        """

        credentials = request_data
        connector_obj = TwitterConnector(credentials)
        timeline_data = connector_obj.get_timeline()
        return timeline_data

    def search_tweet(self, search_string):
        connector_obj = TwitterConnector(search_string)
        timeline_data = connector_obj.get_timeline()
        return timeline_data

    def export_tweets(self, tweet_list=None):
        connector_obj = TwitterConnector("search_string")
        timeline_data = connector_obj.get_timeline()

        with open('tweets_%s.csv' % 'user_id', 'wb') as output_csv:
            csv_writer = csv.DictWriter(output_csv)
            csv_writer.writerows()
            return output_csv
