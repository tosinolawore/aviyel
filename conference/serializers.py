from rest_framework import serializers
from conference.models import Conference

class ConferenceSerializer(serializers.ModelSerializer):
    """Serializer to map the Conference Model instance into JSON format."""
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Conference
        fields = ('id', 'title', 'description', 'start_date','end_date',)