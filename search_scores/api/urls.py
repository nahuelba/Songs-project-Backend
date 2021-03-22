from django.urls import path
from search_scores.api.api import ScoresListAPIView,ArtistListAPIView

urlpatterns = [
    path('scores/', ScoresListAPIView.as_view(), name="scores_api"),
    path('scores/editorial/', ArtistListAPIView.as_view(), name="editorial_api"),
]   