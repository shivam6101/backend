from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Formserializer
from .models import Form

@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
        'Detail_View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks=Form.objects.all().order_by('-id')
    serializer=Formserializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    tasks=Form.objects.get(id=pk)
    serializer=Formserializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskcreate(request):
    serializer=Formserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    tasks=Form.objects.get(id=pk)
    serializer=Formserializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks=Form.objects.get(id=pk)
    tasks.delete()
    return Response('deleted')