from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

import json

from .models import Client, Task
from .serializers import ClientSerializer, TaskSerializer

# Create your views here.


class ClientView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response({"clients": serializer.data})

    def put(self, request):
        data = json.loads(request.body)
        if 'username' not in data.keys():
            return Response({"error": "no username"})
        if 'computer' not in data.keys():
            return Response({"error": "no computer"})
        
        client = Client(username=data['username'],
                        computer=data['computer'])
        client.save()
        return Response({"token": client.id})


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})
    

@csrf_exempt
def connect_client(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid request"})
    if 'id' not in data.keys():
        return JsonResponse({"error": "no id"})
    client = Client.objects.get(id=data["id"])
    if client is None:
        return JsonResponse({"error": "this client does not exist"})
    client.is_connected = True

    client.save()
    
    return JsonResponse({"result": "ok"})


@csrf_exempt
def disconnect_client(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "invalid request"})
    if 'id' not in data.keys():
        return JsonResponse({"error": "no id"})
    client = Client.objects.get(id=data["id"])
    if client is None:
        return JsonResponse({"error": "this client does not exist"})
    client.is_connected = False

    client.save()

    return JsonResponse({"result": "ok"})
