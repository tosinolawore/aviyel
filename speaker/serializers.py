from rest_framework import serializers
from .models import Speaker

class SpeakerSerializer(serializers.ModelSerializer):
    """Serializer to map the Talk Model instance into JSON format."""
    talks =  serializers.PrimaryKeyRelatedField(many=True, queryset=Speaker.objects.all())
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Speaker
        fields = ('id', 'username', 'email', 'first_name','last_name', 'talks','user_type')