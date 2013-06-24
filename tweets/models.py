from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Tweet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    id = models.IntegerField(primary_key = True)
    created_at = models.CharField(blank = False, max_length=100,
                            default = "created at")
    favorited = models.IntegerField(default = 0)
    #Some tweets have more than 140?...
    text = models.CharField(blank = False, max_length = 200,
                            default = "text") 
    in_reply_to_screen_name = models.CharField(max_length = 100,
                            default = "in reply to screen name")
    in_reply_to_user_id = models.CharField(max_length = 100,
                            default = "in reply to user id")
    in_reply_to_status_id = models.CharField(max_length = 100,
                            default = "in reply to status id")
    truncated = models.IntegerField(default = 0)
    source = models.CharField(max_length = 100,
                            default = "source")
    urls = models.CharField(max_length = 200,
                            default = "urls")
    user_mentions = models.CharField(max_length = 100,
                            default = "user_mentions")
    hashtags = models.CharField(max_length = 200,
                            default = "hashtags")
    geo = models.CharField(max_length = 100,
                            default = "geo")
    place = models.CharField(max_length = 100,
                            default = "place")
    coordinates = models.CharField(max_length = 100,
                            default = "coordinates")
    contributors = models.CharField(max_length = 100,
                            default = "contributors")
    retweeted = models.IntegerField(default = 0)
    retweet_count = models.IntegerField(default = 0)
    user_id = models.IntegerField(default = 0)
    user_name = models.CharField(max_length = 100,
                            default = "user name")

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
    id = models.IntegerField(primary_key=True)
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
