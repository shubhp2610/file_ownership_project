from rest_framework import serializers
from .models import File
from django.contrib.auth import get_user_model

User = get_user_model()

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'name', 'file', 'owner', 'original_owner']
        read_only_fields = ['owner', 'original_owner']

class TransferSerializer(serializers.Serializer):
    file_id = serializers.IntegerField()
    to_user_id = serializers.IntegerField()

    def validate(self, data):
        if not File.objects.filter(id=data['file_id']).exists():
            raise serializers.ValidationError({'file_id': 'Invalid file ID'})
        if not User.objects.filter(id=data['to_user_id']).exists():
            raise serializers.ValidationError({'to_user_id': 'Invalid user ID'})
        return data

class RevokeSerializer(serializers.Serializer):
    file_id = serializers.IntegerField()

    def validate_file_id(self, value):
        if not File.objects.filter(id=value).exists():
            raise serializers.ValidationError('Invalid file ID')
        return value