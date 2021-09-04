from django.db import models
from django.contrib.auth import get_user_model


class SpeakerManager(models.Manager):
    def get_query_set(self):
        return super(SpeakerManager, self).get_queryset().filter(
            user_type='SPEAKER')

class Speaker(get_user_model()):
    objects = SpeakerManager()

    class Meta:
        proxy = True
        app_label = 'speaker'
        verbose_name = 'Speaker'

