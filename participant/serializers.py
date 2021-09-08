from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.fields import HiddenField
from talk.models import Talk

class ParticipantSerializer(serializers.ModelSerializer):
    """Serializer to map the Talk Model instance into JSON format."""
    # talks_p =  serializers.PrimaryKeyRelatedField(many=True, queryset=Talk.objects.all(), required=False)
    user_type = serializers.ReadOnlyField()
    
    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password','user_type')
        extra_kwargs = {
            'password':{'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(email=validated_data['email'],     
                password = validated_data['password']  ,username=validated_data['username'],user_type=validated_data['user_type'])
        return user