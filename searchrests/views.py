from searchrests.models import Searchrest
from searchrests.serializers import SearchrestSerializer
from rest_framework import generics
from rest_framework.response import Response
from daemon_connector.interface import DaemonSearch

# Searchrest list.
# We override create to allow creation of job in t2db daemon
class SearchrestList(generics.ListCreateAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer

    def post(self, request, *args, **kwargs):
        daemonSearch = DaemonSearch()
        daemonSearch.newEntry(request.DATA)
        return self.create(request, *args, **kwargs)

#Used only to send default parameters
class SearchrestNew(generics.RetrieveAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer

    def get(self, request, *args, **kwargs):
        searchrest_first = Searchrest()
        serializer = SearchrestSerializer(searchrest_first)
        return Response(serializer.data)

#Override destroy: to allow process destruction in daemon
class SearchrestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer

    def delete(self, request, *args, **kwargs):
        daemonSearch = DaemonSearch()
        key = kwargs["pk"]
        searchrest = Searchrest.objects.get(pk=key)
        serializer = SearchrestSerializer(searchrest)
        daemonSearch.deleteEntry(serializer.data)
        return self.destroy(request, *args, **kwargs)
