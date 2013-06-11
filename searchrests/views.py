from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from searchrests.models import Searchrest
from searchrests.serializers import SearchrestSerializer

@api_view(['GET', 'POST'])
def searchrest_list(request, format = None):
    """
    List all searchrests, or create a new searchrest.
    """
    if request.method == 'GET':
        searchrests = Searchrest.objects.all()
        serializer = SearchrestSerializer(searchrests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SearchrestSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def searchrest_detail(request, pk, format = None):
    """
    Retrieve, update or delete a searchrest instance.
    """              
    try:
        searchrest = Searchrest.objects.get(pk=pk)
    except Searchrest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SearchrestSerializer(searchrest)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SearchrestSerializer(searchrest, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        searchrest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
