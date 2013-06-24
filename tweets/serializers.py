from django.forms import widgets
from rest_framework import serializers
from tweets.models import Tweet, Search, TweetSearch, LANGUAGE_CHOICES, STYLE_CHOICES

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 
                'created_at',
                'favorited',
                'text',
                'in_reply_to_screen_name',
                'in_reply_to_user_id',
                'in_reply_to_status_id',
                'truncated',
                'source',
                'urls',
                'user_mentions',
                'hashtags',
                'geo',
                'place',
                'coordinates',
                'contributors',
                'retweeted',
                'retweet_count',
                'user_id',
                'user_name', 
                'linenos', 'language', 'style')

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 
                'query', 
                'consumer', 
                'consumer_secret',
                'access', 'access_secret', 'linenos', 'language', 'style')

class TweetSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetSearch
        fields = ('id', 
                'tweet_id',
                'search_id', 
                'linenos', 'language', 'style')
