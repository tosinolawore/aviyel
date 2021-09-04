from django.test import TestCase
from .models import Talk
from conference.models import Conference
from speaker.models import Speaker
from participant.models import Participant
from datetime import timedelta, datetime

class TalkTestCase(TestCase):
    """This class defines the test suite for the Conference model."""

    def setUp(self):
        self.conference = Conference(title="Test Conference",description="This conference was for Software Engineers on the importance of TDD.",start_date="2021-09-05",end_date="2021-09-05")
        self.speaker = Speaker(username="TestSpeaker",email="testspeaker@test.com",user_type='SPEAKER')
        self.participant = Participant(username="TestUser",email="testuser@test.com",user_type='PARTICIPANT')
        self.talk = Talk(title="Test Talk", description="Description of a test talk.", duration=timedelta(days=2), conference=self.conference, date=datetime.now())

    def test_create_talk(self):
        """Test the Talk model can create a Talk."""
        old_count = Talk.objects.count()
        self.conference.save()

        # save Talk instance before adding M2M fields
        self.talk.save()

        # save speaker instance and add to Talk model's M2M field
        self.speaker.save()
        self.talk.speakers.add(self.speaker)

        # save participant instance and add to Talk model's M2M field
        self.participant.save()
        self.talk.participants.add(self.participant)

        self.talk.save()
        new_count = Talk.objects.count()
        self.assertNotEqual(old_count, new_count)
        
