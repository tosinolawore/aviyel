from django.db import models
from django.contrib.auth import get_user_model


class ParticipantManager(models.Manager):
    def get_queryset(self):
        return super(ParticipantManager, self).get_queryset().filter(
            user_type='PARTICIPANT')

class Participant(get_user_model()):
    objects = ParticipantManager()

    class Meta:
        proxy = True
        app_label = 'participant'
        verbose_name = "Participant"