from django.urls import path, re_path, include
from speaker.views import SpeakerCreateView, SpeakerDetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      path('speakers/', SpeakerCreateView.as_view(), name="create_speaker"),
      re_path(r'^speakers/(?P<pk>[0-9]+)/$',
        SpeakerDetailsView.as_view(), name="speaker_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)