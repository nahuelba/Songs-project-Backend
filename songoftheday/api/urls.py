from django.urls import path
from .api import SongofthedayListAPIView


urlpatterns = [
    path("songoftheday/", SongofthedayListAPIView.as_view(), name="songoftheday_api")

]
