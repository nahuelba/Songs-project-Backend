from rest_framework.generics import ListAPIView
from songoftheday.models import InterpreterModel, LinksSongsModel, SongModel
from songoftheday.api.serializers import interpreterSerializer, LinkSongsSerializer, SongSerializer
from datetime import datetime




class InterpreterListAPIView(ListAPIView):

    serializer_class = interpreterSerializer

    def get_queryset(self):
        return InterpreterModel.objects.all()



class LinksSongsListAPIView(ListAPIView):

    serializer_class = LinkSongsSerializer

    def get_queryset(self):
        return LinksSongsModel.objects.all()



class SongListAPIView(ListAPIView):

    serializer_class = SongSerializer

    def get_queryset(self):
        return SongModel.objects.all()

class SongofthedayListAPIView(ListAPIView):

    serializer_class = SongSerializer

    def get_queryset(self):
        #get today date
        today = datetime.now().strftime('%d-%m')
        #filter songs
        songoftheday= SongModel.objects.filter(date_song=today)
        
        return songoftheday