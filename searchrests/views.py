# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from searchrests.models import Searchrest
from searchrests.serializers import SearchrestSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def searchrest_list(request):
    """
    List all code searchrests, or create a new searchrest.
    """
    if request.method == 'GET':
        searchrests = Searchrest.objects.all()
        serializer = SearchrestSerializer(searchrests, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SearchrestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def searchrest_detail(request, pk):
    """
    Retrieve, update or delete a code searchrest.
    """
    try:
        searchrest = Searchrest.objects.get(pk=pk)
    except Searchrest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SearchrestSerializer(searchrest)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SearchrestSerializer(searchrest, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        else:
            return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        searchrest.delete()
        return HttpResponse(status=204)
