from django.urls import path, re_path, include
from .views import TalkListView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      re_path(r'^conferences/(?P<conference_id>[0-9]+)/talks/$',
        TalkListView.as_view(), name="create_talk"),
]

urlpatterns = format_suffix_patterns(urlpatterns)