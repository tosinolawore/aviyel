from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Participant

class ParticipantTestCase(TestCase):
    """This class defines the test suite for the Participant model."""

    def setUp(self):
        self.participant = Participant(username="TestUser",email="testuser@test.com",user_type='PARTICIPANT')

    def test_create_participant(self):
        """Test the Participant model can create a participant."""
        old_count = Participant.objects.count()
        self.participant.save()
        new_count = Participant.objects.count()
        self.assertNotEqual(old_count, new_count)