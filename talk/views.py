from rest_framework import generics
from .serializers import TalkSerializer
from .models import Talk
from conference.models import Conference
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class TalkListView(APIView):
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

