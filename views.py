from django.shortcuts import render
from.serializers import movieSerializer,collectionSerializer
from .models import movie , collection
from rest_framework.generics import ListAPIView
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class movieList(ListAPIView):
    queryset = movie.objects.all()
    serializer_class = movieSerializer

class collectionList(ListAPIView):
    queryset = collection.objects.all()
    serializer_class = collectionSerializer



@csrf_exempt
def collection_api(request):
    if request.method =='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=collection.objects.get(id=id)
        stu.delete()
        res = {'msg':'Data Deleted !!!'}
        return JsonResponse(res,safe=False)