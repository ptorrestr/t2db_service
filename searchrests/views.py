from searchrests.models import Searchrest
from searchrests.serializers import SearchrestSerializer
from rest_framework import generics
from rest_framework.response import Response

class SearchrestList(generics.ListCreateAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer

class SearchrestNew(generics.RetrieveAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer

    def get(self, request, *args, **kwargs):
        searchrest_first = Searchrest()
        serializer = SearchrestSerializer(searchrest_first)
        return Response(serializer.data)

class SearchrestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Searchrest.objects.all()
    serializer_class = SearchrestSerializer
