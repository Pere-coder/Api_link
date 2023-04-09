from django.shortcuts import render
from .serializers import NamesSerializer
from .models import Names
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse





# Create your views here.

def Fetch(request):
    pass
    return render(request, 'index.html')




class NamesList(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NamesSerializer
    
    
# class NamesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Names.objects.all()
#     serializer_class = NamesSerializer()
    
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'names': reverse('name-list', request=request, format=format)
    })


