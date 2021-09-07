from django.urls import path, re_path, include
from .views import TalkListView, TalkDetailView, AddParticipantView, DeleteParticipantView, AddSpeakerView, DeleteSpeakerView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      re_path(r'^conferences/(?P<conference_id>[0-9]+)/talks/$',
        TalkListView.as_view(), name="create_talk"),
      re_path(r'^conferences/(?P<conference_id>[0-9]+)/talks/(?P<pk>[0-9]+)/$',
        TalkDetailView.as_view(), name="talk_details"),
      re_path(r'^talks/(?P<talk_id>[0-9]+)/participants/$',
        AddParticipantView.as_view(), name="add_participant"),
      re_path(r'^talks/(?P<talk_id>[0-9]+)/participants/(?P<pk>[0-9]+)/$',
        DeleteParticipantView.as_view(), name="delete_participant"),
      re_path(r'^talks/(?P<talk_id>[0-9]+)/speakers/$',
        AddSpeakerView.as_view(), name="add_speaker"),
      re_path(r'^talks/(?P<talk_id>[0-9]+)speakers/(?P<pk>[0-9]+)/$',
        DeleteSpeakerView.as_view(), name="delete_speaker"),
]

urlpatterns = format_suffix_patterns(urlpatterns)