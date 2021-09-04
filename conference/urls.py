from django.urls import path, re_path, include
from .views import ConferenceCreateView, ConferenceDetailsView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
      path('conferences/', ConferenceCreateView.as_view(), name="create_conference"),
      re_path(r'^conferences/(?P<pk>[0-9]+)/$',
        ConferenceDetailsView.as_view(), name="conference_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)