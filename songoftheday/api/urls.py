from django.urls import path
from .api import InterpreterListAPIView,  LinksSongsListAPIView, SongListAPIView, SongofthedayListAPIView


urlpatterns = [
    path("song/", SongListAPIView.as_view(), name="song_api"),
    path("song/links/", LinksSongsListAPIView.as_view(), name="links_api"),
    path("song/links/interpreter/", InterpreterListAPIView.as_view(), name="interpreter_api"),
    path("songoftheday/", SongofthedayListAPIView.as_view(), name="songoftheday_api")

    

]
