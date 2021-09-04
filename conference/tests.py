from django.test import TestCase
from .models import Conference
from rest_framework.test import APIClient
from rest_framework.views import status
from django.urls import reverse

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


class ConferenceViewTestCase(TestCase):

    """Test suite for the api views."""

    def setUp(self):

        """Define the test client and other test variables."""

        # Initialize client
        self.client = APIClient()

        self.data = {"title":"This is a Test Conference Title.", "description":"This is a Test Conference description.", "start_date":"2021-09-05", "end_date":"2021-09-05"}
        self.response = self.client.post(
            reverse('create_post'),
            self.post_data,
            format="json")

    def test_api_create_conference(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_get_conference(self):
        conference = Conference.objects.get(id=1)
        response = self.client.get(
            '/conference/',
            kwargs={'pk': conference.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, conference)

    def test_api_update_conference(self):
        conference = Conference.objects.get()
        change_conference = {'title': 'A new title'}
        res = self.client.put(
            reverse('conference_details', kwargs={'pk': conference.id}),
            change_conference, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_delete_post(self):
        conference = Conference.objects.get()
        response = self.client.delete(
            reverse('conference_details', kwargs={'pk': conference.id}),
            format='json',
            follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)