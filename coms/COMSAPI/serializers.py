from rest_framework import serializers

class ClientSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    computer = serializers.CharField(max_length=256)
    is_connected = serializers.BooleanField()
