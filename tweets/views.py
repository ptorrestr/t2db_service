from tweets.models import User, Tweet, Search, TweetSearch
from tweets.serializers import UserSerializer
from tweets.serializers import TweetSerializer
from tweets.serializers import SearchSerializer
from tweets.serializers import TweetSearchSerializer
from rest_framework import generics
from rest_framework.response import Response
from daemon_connector.interface import DaemonSearch

###### User ######
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Used only to send default paramaters
class UserNew(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user_first = User()
        serializer = UserSerializer(user_first)
        return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

###### Tweet ######
class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

#Used only to send default parameters
class TweetNew(generics.RetrieveAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get(self, request, *args, **kwargs):
        tweet_first = Tweet()
        serializer = TweetSerializer(tweet_first)
        return Response(serializer.data)

class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


###### Search ######
# We override create to allow creation of job in t2db daemon
class SearchList(generics.ListCreateAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    def post(self, request, *args, **kwargs):
        daemonSearch = DaemonSearch()
        daemonSearch.newEntry(request.DATA)
        return self.create(request, *args, **kwargs)

#Used only to send default parameters
class SearchNew(generics.RetrieveAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    def get(self, request, *args, **kwargs):
        search_first = Search()
        serializer = SearchSerializer(search_first)
        return Response(serializer.data)

#Override destroy: to allow process destruction in daemon
class SearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer

    def delete(self, request, *args, **kwargs):
        daemonSearch = DaemonSearch()
        key = kwargs["pk"]
        search = Search.objects.get(pk=key)
        serializer = SearchSerializer(search)
        daemonSearch.deleteEntry(serializer.data)
        #TODO: Don't destroy search in database, add running attribute
        return self.destroy(request, *args, **kwargs)
        
##### TweetSearch ######
class TweetSearchList(generics.ListCreateAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
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
    
    def get(self, request, *args, **kwargs):
        tweetsearch_first = TweetSearch()
        serializer = TweetSearchSerializer(tweetsearch_first)
        return Response(serializer.data)

class TweetSearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer
