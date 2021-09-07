from rest_framework import serializers
from django.contrib.auth import get_user_model
from talk.models import Talk

class SpeakerSerializer(serializers.ModelSerializer):
    """Serializer to map the Talk Model instance into JSON format."""
    talks_s =  serializers.PrimaryKeyRelatedField(many=True, queryset=Talk.objects.all())
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = get_user_model()
        fields = ('id', 'username', 'email', 'talks_s','user_type')