from rest_framework import generics
from .serializers import TalkSerializer
from .models import Talk
from conference.models import Conference
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from participant.models import Participant
from speaker.models import Speaker
from participant.serializers import ParticipantSerializer
from speaker.serializers import SpeakerSerializer

class TalkListView(APIView):
    """
     List all Talks, create a talk instance.
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

    def get(self, request, format=None):
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response(serializer.data)

    def post(self, request, conference_id, format=None):
        try:
            conference = Conference.objects.get(pk=conference_id)
            talk = Talk(conference=conference)
        except Conference.DoesNotExist:
            raise Http404
        
        serializer = TalkSerializer(talk,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TalkDetailView(APIView):
    """
    Retrieve, update or delete a talk instance.
    """
    def get_object(self, conference_id, pk):
        try:
            conference = Conference.objects.get(pk=conference_id)
            return Talk.objects.get(pk=pk, conference=conference)
        except Talk.DoesNotExist:
            raise Http404

    def get(self, request, conference_id, pk, format=None):
        talk = self.get_object(conference_id, pk)
        serializer = TalkSerializer(talk)
        return Response(serializer.data)

    def put(self, request, conference_id, pk, format=None):
        talk = self.get_object(conference_id, pk)
        serializer = TalkSerializer(talk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, conference_id, pk, format=None):
        talk = self.get_object(conference_id, pk)
        talk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddParticipantView(APIView):
    """
     Add Participant to a Talk.
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

    def post(self, request, talk_id, format=None):
        try:
            talk = Talk.objects.get(pk=talk_id)

            # get participant id from post data
            participant_id = request.data["participant_id"]
        except Talk.DoesNotExist:
            raise Http404

        # get participant instance
        participant = Participant.objects.get(pk=participant_id)

        # add participant to talk 
        talk.participants.add(participant)
        talk.save()

        #serialize result
        serializer = TalkSerializer(talk)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DeleteParticipantView(APIView):
    """
     Delete Participant from a Talk.
    """
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

    def delete(self, request, talk_id, pk, format=None):
        try:
            talk = Talk.objects.get(pk=talk_id)
            participant = Participant.objects.get(pk=pk)
        except Talk.DoesNotExist:
            raise Http404

        # add participant to talk 
        talk.participants.remove(participant)
        talk.save()

        return Response(status=status.HTTP_204_NO_CONTENT)