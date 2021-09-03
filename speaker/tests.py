from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Speaker

class SpeakerTestCase(TestCase):
    """This class defines the test suite for the Speaker model."""

    def setUp(self):
        self.speaker = Speaker(username="TestSpeaker",email="testspeaker@test.com",user_type='SPEAKER')

    def test_create_speaker(self):
        """Test the Speaker model can create a Speaker."""
        old_count = Speaker.objects.count()
        self.speaker.save()
        new_count = Speaker.objects.count()
        self.assertNotEqual(old_count, new_count)