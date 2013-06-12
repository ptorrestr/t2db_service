from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from searchrests import views

urlpatterns = patterns('',
    url(r'^searchrests$', views.SearchrestList.as_view()),
    url(r'^searchrests/new$', views.SearchrestNew.as_view()),
#    url(r'^searchrests/$', views.SearchrestList.as_view()),
    url(r'^searchrests/(?P<pk>[0-9]+)$', views.SearchrestDetail.as_view()),
#    url(r'^searchrests/(?P<pk>[0-9]+)/$', views.SearchrestDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
