from django.contrib.auth.models import User
from rest_framework import serializers
from notes.serializers import NotesSerializer

class UserSerializer(serializers.ModelSerializer):
    notes = NotesSerializer(many=True, read_only=True)
    class Meta:
        model= User
        fields= ['url','id', 'username', 'email', 'notes']
