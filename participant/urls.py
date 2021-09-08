from django.urls import path, re_path, include
from .views import ParticipantCreateView, ParticipantDetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      path('participants/', ParticipantCreateView.as_view(), name="create_participant"),
      re_path(r'^participants/(?P<pk>[0-9]+)/$',
        ParticipantDetailsView.as_view(), name="participant_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)