from rest_framework import serializers

class ClientSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=256)
    username = serializers.CharField(max_length=256)
    computer = serializers.CharField(max_length=256)
    is_connected = serializers.BooleanField()


class TaskSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=256)
    name = serializers.CharField(max_length=256)
    client = serializers.CharField(max_length=256, source='client.id')
