from rest_framework import generics
from .serializers import ConferenceSerializer
from .models import Conference
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class ConferenceCreateView(generics.ListCreateAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

    def perform_create(self, serializer):
        """Save the Conference data when creating a new Conference."""
        serializer.save()

class ConferenceDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer