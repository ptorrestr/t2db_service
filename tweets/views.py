from tweets.models import User, Tweet, Search, SearchRun, TweetSearch
from tweets.serializers import UserSerializer
from tweets.serializers import TweetSerializer
from tweets.serializers import SearchSerializer
from tweets.serializers import SearchRunSerializer
from tweets.serializers import TweetSearchSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from daemon_connector.interface import DaemonSearch

###### User ######
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#Used only to send default paramaters
class UserNew(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        user_first = User()
        serializer = UserSerializer(user_first)
        return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

###### Tweet ######
class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Tweet.objects.all()
        search_id = self.request.QUERY_PARAMS.get('search_id', None)
        last = self.request.QUERY_PARAMS.get('last', None)
        if search_id is not None:
            if last is not None:
                #Return the last 10 tweets
                queryset = queryset.filter(tweetSearch__search_id = search_id)[:10]
            else:
                #Return all tweets
                queryset = queryset.filter(tweetSearch__search_id = search_id)
        return queryset

#Used only to send default parameters
class TweetNew(generics.RetrieveAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        tweet_first = Tweet()
        serializer = TweetSerializer(tweet_first)
        return Response(serializer.data)

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

###### Search ######
# We override create to allow creation of job in t2db daemon
class SearchList(generics.ListCreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

#Used only to send default parameters
class SearchNew(generics.RetrieveAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        search_first = Search()
        serializer = SearchSerializer(search_first)
        return Response(serializer.data)

#Override destroy: to allow process destruction in daemon
class SearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

##### SearchRun ######
class SearchRunList(generics.ListCreateAPIView):
    queryset = SearchRun.objects.all()
    serializer_class = SearchRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        search_id = request.DATA["search"]
        search = Search.objects.get(pk = search_id)
        serializer = SearchSerializer(search)
        DaemonSearch().newEntry(serializer.data)
        return self.create(request, *args, **kwargs)

class SearchRunNew(generics.RetrieveAPIView):
    queryset = SearchRun.objects.all()
    serializer_class = SearchRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        searchrun_first = SearchRun()
        serializer = SearchRunSerializer(searchrun_first)
        return Response(serializer.data)

class SearchRunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchRun.objects.all()
    serializer_class = SearchRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        key = kwargs["pk"]
        searchrun = SearchRun.objects.get(pk = key)
        search = Search.objects.get(pk = searchrun.search.id)
        serializer = SearchSerializer(search)
        DaemonSearch().deleteEntry(serializer.data)
        return self.destroy(request, *args, **kwargs)

##### TweetSearch ######
class TweetSearchList(generics.ListCreateAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = TweetSearch.objects.all()
        search_id = self.request.QUERY_PARAMS.get('search_id', None)
        tweet_id = self.request.QUERY_PARAMS.get('tweet_id', None)
        if search_id is not None:
            if tweet_id is not None:
                queryset = queryset.filter(search_id = search_id,
                                     tweet_id = tweet_id)
            else:
                #return only the last 10 tweets id
                queryset = queryset.order_by('-created').filter(search_id = search_id)[:10]
        return queryset

class TweetSearchNew(generics.RetrieveAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        tweetsearch_first = TweetSearch()
        serializer = TweetSearchSerializer(tweetsearch_first)
        return Response(serializer.data)

class TweetSearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

##### SetTweet #####
#class TweetSearchDetail(generics.RetrieveAPIView):
#    queryset = Tweet.objects.all()
#    seralizer_class = TweetSerializer
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#    def get(self, request, *args, **kwargs):
#        se
