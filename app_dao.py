"""
    Module that houses all database operations
"""

from mysql.connector import connect, Error


class AppDAO:
    def __init__(self):
        self.conn = self.__get_conn()

    def __get_conn(self):
        return
        return connect(host="localhost",
                            user="username",
                            password="password",
                            database="twitter_db")

    def save_tweets(self):
        return
        query = "INSERT into tweets(user_id, tweet_info, created_by, created_datetime) values"
        with self.conn.cursor() as cursor:
            cursor.execute(query)

    def search_tweet(self):
        return
        query = "SELECT * from tweets where user_id = %s and tweet_info rlike %s"
        with self.conn.cursor() as cursor:
            return cursor.fetchall(query)
