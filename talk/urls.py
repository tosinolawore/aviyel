from django.urls import path, re_path, include
from .views import TalkListView, TalkDetailView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      re_path(r'^conferences/(?P<conference_id>[0-9]+)/talks/$',
        TalkListView.as_view(), name="create_talk"),
      re_path(r'^conferences/(?P<conference_id>[0-9]+)/talks/(?P<pk>[0-9]+)/$',
        TalkDetailView.as_view(), name="talk_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)