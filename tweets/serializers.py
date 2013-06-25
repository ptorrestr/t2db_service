from django.forms import widgets
from rest_framework import serializers
from tweets.models import User, Tweet, Search, TweetSearch 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                'created_at',
                'name',
                'screen_name',
                'location',
                'description',
                'profile_image_url',
                'profile_image_url_https',
                'profile_background_tile',
                'profile_background_image_url',
                'profile_background_color',
                'profile_sidebar_fill_color',
                'profile_sidebar_border_color',
                'profile_link_color',
                'profile_text_color',
                'protected',
                'utc_offset',
                'time_zone',
                'followers_count',
                'friends_count',
                'statuses_count',
                'favourites_count',
                'url',
                'geo_enabled',
                'verified',
                'lang',
                'notifications',
                'contributors_enabled',
                'listed_count',
                'linenos', 'language', 'style')

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
                'linenos', 'language', 'style')

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ('id', 
                'query', 
                'consumer', 
                'consumer_secret',
                'access',
                'access_secret',
                'linenos', 'language', 'style')

class TweetSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetSearch
        fields = ('id', 
                'tweet_id',
                'search_id', 
                'linenos', 'language', 'style')
