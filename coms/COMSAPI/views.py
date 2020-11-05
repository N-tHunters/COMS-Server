from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from .models import Client
from .serializers import ClientSerializer

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


def connect_client(request):
    pass

def disconnect_client(request):
    pass
