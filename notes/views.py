from django.shortcuts import render
from .serializers import NotesSerializer
from rest_framework import permissions, viewsets
from .models import Notes
# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    permission_classes = [permissions.IsAuthenticated]
    


