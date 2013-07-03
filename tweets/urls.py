from django.conf.urls import patterns, url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from tweets import views

urlpatterns = patterns('',

    url(r'^users$', views.UserList.as_view()),
    url(r'^users/new$', views.UserNew.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),

    url(r'^tweets$', views.TweetList.as_view()),
    url(r'^tweets/new$', views.TweetNew.as_view()),
    url(r'^tweets/(?P<pk>[0-9]+)$', views.TweetDetail.as_view()),

    url(r'^searches$', views.SearchList.as_view()),
    url(r'^searches/new$', views.SearchNew.as_view()),
    url(r'^searches/(?P<pk>[0-9]+)$', views.SearchDetail.as_view()),

    url(r'^tweetsearches$', views.TweetSearchList.as_view()),
    url(r'^tweetsearches/new$', views.TweetSearchNew.as_view()),    
    url(r'^tweetsearches/(?P<pk>[0-9]+)$', views.TweetSearchDetail.as_view()),

    #url(r'^settweets/(?P<pk>[0-9]+)$', views.SetTweetDetail.as_view()),

    #Authentication by browser
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns = format_suffix_patterns(urlpatterns)
