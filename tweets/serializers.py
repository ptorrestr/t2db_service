from django.forms import widgets
from rest_framework import serializers
from tweets.models import User, Tweet, Search, SearchRun, TweetSearch 

class TweetSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetSearch
        fields = ('id', 
                'tweet',
                'search',
                )

class TweetSerializer(serializers.ModelSerializer):
    tweetSearch = TweetSearchSerializer(
        many = True,
        read_only = True,
    )

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
                'user',
                'tweetSearch',
                )

class SearchRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchRun
        fields = ('id',
                'search',
                )

class SearchSerializer(serializers.ModelSerializer):
    tweetSearch = TweetSearchSerializer(
        many = True,
        read_only = True,
    )

    searchrun = SearchRunSerializer(
        read_only = True,
    )

    class Meta:
        model = Search
        fields = ('id', 
                'query', 
                'consumer', 
                'consumer_secret',
                'access',
                'access_secret',
                'tweetSearch',
                'searchrun',
                )

class UserSerializer(serializers.ModelSerializer):
    tweet = TweetSerializer(
        many = True,
        read_only = True,
    )

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
                'tweet',
                'linenos', 'language', 'style')
