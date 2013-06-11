from django.conf.urls import patterns, url

urlpatterns = patterns('searchrests.views',
    url(r'^searchrests/$', 'searchrest_list'),
    url(r'^searchrests/(?P<pk>[0-9]+)/$', 'searchrest_detail'),
)
