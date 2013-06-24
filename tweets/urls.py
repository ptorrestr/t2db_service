from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tweets import views

urlpatterns = patterns('',
    url(r'^tweets$', views.TweetList.as_view()),
    url(r'^tweets/new$', views.TweetNew.as_view()),
    url(r'^tweets/(?P<pk>[0-9]+)$', views.TweetDetail.as_view()),

    url(r'^searches$', views.SearchList.as_view()),
    url(r'^searches/new$', views.SearchNew.as_view()),
    url(r'^searches/(?P<pk>[0-9]+)$', views.SearchDetail.as_view()),

    url(r'^tweetsearches$', views.TweetSearchList.as_view()),
    url(r'^tweetsearches/new$', views.TweetSearchNew.as_view()),    
    url(r'^tweetsearches/(?P<pk>[0-9]+)$', views.TweetSearchDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
