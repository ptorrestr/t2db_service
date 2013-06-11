from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Searchrest(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    
    #blank: The value could not be empty
    #db_index: Create an index in the database for the field
    #unique: Cannot be two search_id with the same value
    #max_length: Maximum string size
    search_id = models.IntegerField(db_index=True, unique=True)
    query = models.CharField(max_length=140, blank=False)
    consumer = models.CharField(max_length=100, blank=False)
    consumer_secret = models.CharField(max_length=100, blank=False)
    access = models.CharField(max_length=100, blank=False)
    access_secret = models.CharField(max_length=100, blank=False)
    
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
