from django.db import models
from conference.models import Conference
from participant.models import Participant
from speaker.models import Speaker

class Talk(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    duration = models.DurationField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    speakers = models.ManyToManyField(Speaker, related_name="talks_s", blank=True)
    participants = models.ManyToManyField(Participant, related_name="talks_p", blank=True)
    date = models.DateTimeField()

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)