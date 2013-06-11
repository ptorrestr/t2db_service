from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('searchrests.views',
    url(r'^searchrests/$', 'searchrest_list'),
    url(r'^searchrests/(?P<pk>[0-9]+)/$', 'searchrest_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
