from rest_framework import generics
from .serializers import SpeakerSerializer
from .models import Speaker
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class SpeakerCreateView(generics.ListCreateAPIView):
    queryset = Speaker.objects.filter(user_type='SPEAKER')
    serializer_class = SpeakerSerializer

    def perform_create(self, serializer):
        """Save the Speaker data when creating a new Speaker."""
        serializer.save(user_type="SPEAKER")

class SpeakerDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.filter(user_type='SPEAKER')
    serializer_class = SpeakerSerializer