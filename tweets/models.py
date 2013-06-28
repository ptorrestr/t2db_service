from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Some user data are not included. See twitter user.
class User(models.Model):
    created = models.DateTimeField(auto_now_add = True)

    id = models.BigIntegerField(primary_key = True)
    created_at = models.CharField(blank = False,
                            max_length = 200)
    name = models.CharField(blank = False,
                            max_length = 200)
    screen_name = models.CharField(max_length = 200,
                            default = "screen name")
    location = models.CharField(blank = True,
                            max_length = 200,
                            default = "location")
    description = models.CharField(blank = True,
                            max_length = 200,
                            default = "description")
    profile_image_url = models.CharField(blank = True,
                            max_length = 1024,
                            default = "profile image url")
    profile_image_url_https = models.CharField(blank = True,
                            max_length = 1024,
                            default = "profile image url https")
    profile_background_tile = models.IntegerField(default = 0)
    profile_background_image_url = models.CharField(blank = True,
                            max_length = 1024,
                            default = "profile background image url")
    profile_background_color = models.CharField(blank = True,
                            max_length = 200,
                            default = "profile background color")
    profile_sidebar_fill_color = models.CharField(blank = True,
                            max_length = 200,
                            default = "profile sidebar fill color")
    profile_sidebar_border_color = models.CharField(blank = True,
                            max_length = 200,
                            default = "profile sidebar border color")
    profile_link_color = models.CharField(blank = True,
                            max_length = 200,
                            default = "profile link color")
    profile_text_color = models.CharField(blank = True,
                            max_length = 200,
                            default = "profile text color")
    protected = models.IntegerField(default = 0)
    utc_offset = models.IntegerField(default = 0)
    time_zone = models.CharField(blank = True,
                            max_length = 200,
                            default = "time zone")
    followers_count = models.IntegerField(default = 0)
    friends_count = models.IntegerField(default = 0)
    statuses_count = models.IntegerField(default = 0)
    favourites_count = models.IntegerField(default = 0)
    url = models.CharField(blank = True,
                            max_length = 200,
                            default = "url")
    geo_enabled = models.IntegerField(default = 0)
    verified = models.IntegerField(default = 0)
    lang = models.CharField(blank = True,
                            max_length = 200,
                            default = "lang")
    notifications = models.IntegerField(default = 0)
    contributors_enabled = models.IntegerField(default = 0)
    listed_count = models.IntegerField(default = 0)

    #Foreign Key

    #Find for what rason this values must be added?    
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                            default='python',
                            max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                            default='friendly',
                            max_length=100)

    class Meta:
        ordering = ('created',)


class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.BigIntegerField(primary_key = True)
    created_at = models.CharField(blank = False, max_length=100,
                            default = "created at")
    favorited = models.IntegerField(default = 0)
    #Some tweets have more than 140?...
    text = models.CharField(blank = False, max_length = 200,
                            default = "text") 
    in_reply_to_screen_name = models.CharField(blank = True,
                            max_length = 200,
                            default = "in reply to screen name")
    in_reply_to_user_id = models.CharField(blank = True,
                            max_length = 200,
                            default = "in reply to user id")
    in_reply_to_status_id = models.CharField(blank = True,
                            max_length = 200,
                            default = "in reply to status id")
    truncated = models.IntegerField(default = 0)
    source = models.CharField(blank = True,
                            max_length = 200,
                            default = "source")
    urls = models.CharField(blank = True,
                            max_length = 200,
                            default = "urls")
    user_mentions = models.CharField(blank = True,
                            max_length = 200,
                            default = "user_mentions")
    hashtags = models.CharField(blank = True,
                            max_length = 200,
                            default = "hashtags")
    geo = models.CharField(blank = True,
                            max_length = 200,
                            default = "geo")
    place = models.CharField(blank = True,
                            max_length = 200,
                            default = "place")
    coordinates = models.CharField(blank = True,
                            max_length = 200,
                            default = "coordinates")
    contributors = models.CharField(blank = True,
                            max_length = 200,
                            default = "contributors")
    retweeted = models.IntegerField(default = 0)
    retweet_count = models.IntegerField(default = 0)

    #Foreign Key
    user_id = models.ForeignKey(User)
    
    #Find for what rason this values must be added?    
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                            default='python',
                            max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                            default='friendly',
                            max_length=100)

    class Meta:
        ordering = ('created',)

class Search(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.BigIntegerField(primary_key = True)
    query = models.CharField(max_length = 140,
                            blank = False)
    consumer = models.CharField(max_length=100,
                            blank = False)
    consumer_secret = models.CharField(max_length = 100,
                            blank = False)
    access = models.CharField(max_length = 100,
                            blank = False)
    access_secret = models.CharField(max_length = 100,
                            blank = False)

    #Foreign Key
    
    #Find for what rason this values must be added?    
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                            default='python',
                            max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                            default='friendly',
                            max_length=100)

    class Meta:
        ordering = ('created',)

class TweetSearch(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size

    #Foreign Key 
    tweet_id = models.ForeignKey(Tweet)
    search_id = models.ForeignKey(Search)

    #Find for what rason this values must be added?    
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                            default='python',
                            max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                            default='friendly',
                            max_length=100)

    class Meta:
        ordering = ('created',)
