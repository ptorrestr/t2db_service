from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Some user data are not included. See twitter user.
class User(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    # INTEGERS
    id = models.BigIntegerField(primary_key = True)
    utc_offset = models.IntegerField(blank = True, null = True)
    followers_count = models.IntegerField(blank = True, null = True)
    friends_count = models.IntegerField(blank = True, null = True)
    statuses_count = models.IntegerField(blank = True, null = True)
    favourites_count = models.IntegerField(blank = True, null = True)
    listed_count = models.IntegerField(blank = True, null = True)
    # STRINGS
    created_at = models.CharField(blank = False, max_length = 200)
    name = models.CharField(blank = False, max_length = 200)
    screen_name = models.CharField(blank = True, null = True, max_length = 200)
    location = models.CharField(blank = True, null = True, max_length = 200)
    description = models.CharField(blank = True, null = True, max_length = 200)
    profile_image_url = models.CharField(blank = True, null = True, max_length = 1024)
    profile_image_url_https = models.CharField(blank = True, null = True, max_length = 1024)
    profile_background_image_url = models.CharField(blank = True, null = True, max_length = 1024)
    profile_background_color = models.CharField(blank = True, null = True, max_length = 200)
    profile_sidebar_fill_color = models.CharField(blank = True, null = True, max_length = 200)
    profile_sidebar_border_color = models.CharField(blank = True, null = True, max_length = 200)
    profile_link_color = models.CharField(blank = True, null = True, max_length = 200)
    profile_text_color = models.CharField(blank = True, null = True, max_length = 200)
    time_zone = models.CharField(blank = True, null = True, max_length = 200)
    url = models.CharField(blank = True, null = True, max_length = 200)
    lang = models.CharField(blank = True, null = True, max_length = 200)
    # BOOLS
    profile_background_tile = models.BooleanField(blank = True)
    protected = models.BooleanField(blank = True)
    geo_enabled = models.BooleanField(blank = True)
    verified = models.BooleanField(blank = True)
    notifications = models.BooleanField(blank = True)
    contributors_enabled = models.BooleanField(blank = True)

    #Foreign Key

    #Ordering priorities
    class Meta:
        ordering = ('created',)


class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.BigIntegerField(primary_key = True)
    retweet_count = models.IntegerField(blank = True, null = True)
    created_at = models.CharField(max_length=100)
    text = models.CharField(blank = True, null = True, max_length = 200)
    in_reply_to_screen_name = models.CharField(blank = True, null = True, max_length = 200)
    in_reply_to_user_id = models.BigIntegerField(blank = True, null = True)
    in_reply_to_status_id = models.BigIntegerField(blank = True, null = True)
    source = models.CharField(blank = True, null = True, max_length = 200)
    urls = models.CharField(blank = True, null = True, max_length = 2048)
    user_mentions = models.CharField(blank = True, null = True, max_length = 2048)
    hashtags = models.CharField(blank = True, null = True, max_length = 2048)
    place = models.CharField(blank = True, null = True, max_length = 200)
    coordinates = models.CharField(blank = True, null = True, max_length = 200)
    contributors = models.CharField(blank = True, null = True, max_length = 200)
    favorited = models.BooleanField(blank = True)
    truncated = models.BooleanField(blank = True)
    retweeted = models.BooleanField(blank = True)

    #Foreign Key
    user = models.ForeignKey(User, related_name = 'tweet')

    class Meta:
        ordering = ('created',)

class Search(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.BigIntegerField(primary_key = True)
    query = models.CharField(blank = False, max_length = 140)
    consumer = models.CharField(blank = False, max_length=100)
    consumer_secret = models.CharField(blank = False, max_length = 100)
    access = models.CharField(blank = False, max_length = 100)
    access_secret = models.CharField(blank = False, max_length = 100)
    class Meta:
        ordering = ('created',)

class SearchRun(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    #Foreign Key
    search = models.ForeignKey(Search, 
                            related_name = 'searchrun')
    class Meta:
        ordering = ('created',)


class TweetSearch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size

    #Foreign Key 
    tweet = models.ForeignKey(Tweet, related_name = 'tweetSearch')
    search = models.ForeignKey(Search, related_name = 'tweetSearch')

    class Meta:
        ordering = ('created',)

class Streaming(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.BigIntegerField(primary_key = True)
    query = models.CharField(blank = False, max_length = 140)
    consumer = models.CharField(blank = False, max_length = 100)
    consumer_secret = models.CharField(blank = False, max_length = 100)
    access = models.CharField(blank = False, max_length = 100)
    access_secret = models.CharField(blank = False, max_length = 100)

    class Meta:
        ordering = ('created',)

class StreamingRun(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    #Foreign Key
    streaming = models.ForeignKey(Streaming, 
                            related_name = 'streamingrun')
    class Meta:
        ordering = ('created',)


class TweetStreaming(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size

    #Foreign Key 
    tweet = models.ForeignKey(Tweet, related_name = 'tweetStreaming')
    streaming = models.ForeignKey(Streaming, related_name = 'tweetStreaming')

    class Meta:
        ordering = ('created',)
