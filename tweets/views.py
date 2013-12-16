from tweets.models import User
from tweets.models import Tweet
from tweets.models import Search
from tweets.models import SearchRun
from tweets.models import TweetSearch
from tweets.models import Streaming
from tweets.models import StreamingRun
from tweets.models import TweetStreaming
from tweets.serializers import UserSerializer
from tweets.serializers import TweetSerializer
from tweets.serializers import SearchSerializer
from tweets.serializers import SearchRunSerializer
from tweets.serializers import TweetSearchSerializer
from tweets.serializers import StreamingSerializer
from tweets.serializers import StreamingRunSerializer
from tweets.serializers import TweetStreamingSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from daemon_connector.interface import DaemonSearch

###### User ######
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(User.objects.all(), many = True,
            data = request.DATA, allow_add_remove = True)
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def post(self, request, *args, **kwargs):
        serializer = TweetSerializer(Tweet.objects.all(), many = True,
            data = request.DATA, allow_add_remove = True)
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Tweet.objects.all()
        search_id = self.request.QUERY_PARAMS.get('search_id', None)
        streaming_id = self.request.QUERY_PARAMS.get('streaming_id', None)
        last = self.request.QUERY_PARAMS.get('last', None)
        if search_id is not None:
            if last is not None:
                #Return the last 10 tweets
                queryset = queryset.order_by('-created').filter(tweetSearch__search_id = search_id)[:10]
            else:
                #Return all tweets
                queryset = queryset.filter(tweetSearch__search_id = search_id)
        elif streaming_id is not None:
            if last is not None:
                #Return the last 10 tweets for streaming
                queryset = queryset.order_by('-created').filter(tweetStreaming__streaming_id = streaming_id)[:10]
            else:
                #REturn all teets for streaming
                queryset = queryset.filter(tweetStreaming__streaming_id = streaming_id)
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

    def post(self, request, *args, **kwargs):
        serializer = SearchSerializer(Search.objects.all(), many = True, 
            data = request.DATA, allow_add_remove = True)        
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    def get_queryset(self):
        queryset = SearchRun.objects.all()
        search_id = self.request.QUERY_PARAMS.get('search_id', None)
        if search_id is not None:
            queryset = queryset.filter(search = search_id)
        return queryset

    def post(self, request, *args, **kwargs):
        search_id = request.DATA["search"]
        search = Search.objects.get(pk = search_id)
        serializer = SearchSerializer(search)
        DaemonSearch().newEntry(serializer.data, "search")
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
        DaemonSearch().deleteEntry(serializer.data, "search")
        return self.destroy(request, *args, **kwargs)

##### TweetSearch ######
class TweetSearchList(generics.ListCreateAPIView):
    queryset = TweetSearch.objects.all()
    serializer_class = TweetSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = TweetSearchSerializer(TweetSearch.objects.all(), many = True, 
            data = request.DATA, allow_add_remove = True)        
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

###### Streaming ######
class StreamingList(generics.ListCreateAPIView):
    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = StreamingSerializer(Streaming.objects.all(), many = True, 
            data = request.DATA, allow_add_remove = True)        
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Used only to send default parameters
class StreamingNew(generics.RetrieveAPIView):
    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        streaming_first = Streaming()
        serializer = StreamingSerializer(streaming_first)
        return Response(serializer.data)

class StreamingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Streaming.objects.all()
    serializer_class = StreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

##### StreamingRun ######
class StreamingRunList(generics.ListCreateAPIView):
    queryset = StreamingRun.objects.all()
    serializer_class = StreamingRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = StreamingRun.objects.all()
        streaming_id = self.request.QUERY_PARAMS.get('streaming_id', None)
        if streaming_id is not None:
            queryset = queryset.filter(streaming = streaming_id)
        return queryset

    def post(self, request, *args, **kwargs):
        streaming_id = request.DATA["streaming"]
        streaming = Streaming.objects.get(pk = streaming_id)
        serializer = StreamingSerializer(streaming)
        DaemonSearch().newEntry(serializer.data, "streaming")
        return self.create(request, *args, **kwargs)

class StreamingRunNew(generics.RetrieveAPIView):
    queryset = StreamingRun.objects.all()
    serializer_class = StreamingRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        streamingrun_first = StreamingRun()
        serializer = StreamingRunSerializer(streamingrun_first)
        return Response(serializer.data)

class StreamingRunDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamingRun.objects.all()
    serializer_class = StreamingRunSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def delete(self, request, *args, **kwargs):
        key = kwargs["pk"]
        streamingrun = StreamingRun.objects.get(pk = key)
        streaming = Streaming.objects.get(pk = streamingrun.streaming.id)
        serializer = StreamingSerializer(streaming)
        DaemonSearch().deleteEntry(serializer.data, "streaming")
        return self.destroy(request, *args, **kwargs)

##### TweetStreaming ######
class TweetStreamingList(generics.ListCreateAPIView):
    queryset = TweetStreaming.objects.all()
    serializer_class = TweetStreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = TweetStreamingSerializer(TweetStreaming.objects.all(), many = True, 
            data = request.DATA, allow_add_remove = True)        
        if serializer.is_valid():
            [serializer.save_object(item) for item in serializer.object]
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = TweetStreaming.objects.all()
        streaming_id = self.request.QUERY_PARAMS.get('streaming_id', None)
        tweet_id = self.request.QUERY_PARAMS.get('tweet_id', None)
        if streaming_id is not None:
            if tweet_id is not None:
                queryset = queryset.filter(streaming_id = streaming_id,
                                     tweet_id = tweet_id)
            else:
                #return only the last 10 tweets id
                queryset = queryset.order_by('-created').filter(streaming_id = streaming_id)[:10]
        return queryset

class TweetStreamingNew(generics.RetrieveAPIView):
    queryset = TweetStreaming.objects.all()
    serializer_class = TweetStreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def get(self, request, *args, **kwargs):
        tweetstreaming_first = TweetStreaming()
        serializer = TweetStreamingSerializer(tweetstreaming_first)
        return Response(serializer.data)

class TweetStreamingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetStreaming.objects.all()
    serializer_class = TweetStreamingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

