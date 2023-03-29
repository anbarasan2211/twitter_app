# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import emoji

from flask import Flask, request
from flask import render_template

from handler import AppHandler

app = Flask(__name__)


@app.get('/')
def home():
    """
        Home page
    """

    return render_template('login.html')


@app.post('/')
def login():
    """
        Controller that handles the login and timeline sync
    """

    request_data = request.form.to_dict()
    app_handler = AppHandler()
    tweet_data = app_handler.sync_tweets(request_data)
    return render_template('view_tweets.html', tweet_data=tweet_data['data'])


@app.post('/search/')
def search():
    """
        Controller that handles the search_tweet
    """

    request_data = request.form.to_dict()
    app_handler = AppHandler()
    return app_handler.search_tweet(request_data['search_string'])


@app.post('/export/')
def export():
    """
        Controller that handles the export/download of tweets
    """

    request_data = request.form.to_dict()
    app_handler = AppHandler()
    return app_handler.export_tweets(request_data)


@app.template_filter('emojify')
def emoji_filter(s):
    return emoji.emojize(s)
