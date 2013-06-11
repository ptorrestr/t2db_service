from django.forms import widgets
from rest_framework import serializers
from searchrests.models import Searchrest, LANGUAGE_CHOICES, STYLE_CHOICES

class SearchrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searchrest
        fields = ('id', 'search_id', 'query', 'consumer', 'consumer_secret',
                'access', 'access_secret', 'linenos', 'language', 'style')
