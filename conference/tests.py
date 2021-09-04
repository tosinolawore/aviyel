from django.test import TestCase
from .models import Conference

class ConferenceTestCase(TestCase):
    """This class defines the test suite for the Conference model."""

    def setUp(self):
        self.conference = Conference(title="Test Conference",description="This conference was for Software Engineers on the importance of TDD.",start_date="2021-09-05",end_date="2021-09-05")

    def test_create_conference(self):
        """Test the Conference model can create a conference."""
        old_count = Conference.objects.count()
        self.conference.save()
        new_count = Conference.objects.count()
        self.assertNotEqual(old_count, new_count)
