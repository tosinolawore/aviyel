from rest_framework import generics
from .serializers import ParticipantSerializer
from .models import Participant
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class ParticipantCreateView(generics.ListCreateAPIView):
    queryset = Participant.objects.filter(user_type='PARTICIPANT')
    serializer_class = ParticipantSerializer

    def perform_create(self, serializer):
        """Save the Participant data when creating a new Participant."""
        serializer.save(user_type="PARTICIPANT")

class ParticipantDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participant.objects.filter(user_type='PARTICIPANT')
    serializer_class = ParticipantSerializer