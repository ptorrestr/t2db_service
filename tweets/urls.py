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

    url(r'^searchruns$', views.SearchRunList.as_view()),
    url(r'^searchruns/new$', views.SearchRunNew.as_view()),
    url(r'^searchruns/(?P<pk>[0-9]+)$', views.SearchRunDetail.as_view()),

    url(r'^tweetsearches$', views.TweetSearchList.as_view()),
    url(r'^tweetsearches/new$', views.TweetSearchNew.as_view()),    
    url(r'^tweetsearches/(?P<pk>[0-9]+)$', views.TweetSearchDetail.as_view()),

    url(r'^streamings$', views.StreamingList.as_view()),
    url(r'^streamings/new$', views.StreamingNew.as_view()),
    url(r'^streamings/(?P<pk>[0-9]+)$', views.StreamingDetail.as_view()),

    url(r'^streamingruns$', views.StreamingRunList.as_view()),
    url(r'^streamingruns/new$', views.StreamingRunNew.as_view()),
    url(r'^streamingruns/(?P<pk>[0-9]+)$', views.StreamingRunDetail.as_view()),

    url(r'^tweetstreamings$', views.TweetStreamingList.as_view()),
    url(r'^tweetstreamings/new$', views.TweetStreamingNew.as_view()),    
    url(r'^tweetstreamings/(?P<pk>[0-9]+)$', views.TweetStreamingDetail.as_view()),


    #Authentication by browser
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

)

urlpatterns = format_suffix_patterns(urlpatterns)
