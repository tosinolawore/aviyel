from rest_framework import serializers
from .models import Talk
from speaker.serializers import SpeakerSerializer
from participant.serializers import ParticipantSerializer

class TalkSerializer(serializers.ModelSerializer):
    """Serializer to map the Talk Model instance into JSON format."""
    speakers = SpeakerSerializer(many=True, required=False, read_only=True)
    participants = ParticipantSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Talk
        fields = ('id', 'title', 'description', 'duration','conference','speakers','participants', 'date')