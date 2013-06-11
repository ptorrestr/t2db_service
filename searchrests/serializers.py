from django.forms import widgets
from rest_framework import serializers
from searchrests.models import Searchrest, LANGUAGE_CHOICES, STYLE_CHOICES

class SearchrestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searchrest
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
