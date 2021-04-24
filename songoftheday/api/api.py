from rest_framework.generics import ListAPIView
from songoftheday.models import InterpreterModel, LinksSongsModel, SongModel
from songoftheday.api.serializers import SongSerializer
from datetime import datetime





class SongofthedayListAPIView(ListAPIView):

    serializer_class = SongSerializer

    def get_queryset(self):
        #get today date
        today = datetime.now().strftime('%d-%m')
        #filter songs
        songoftheday= SongModel.objects.filter(date_song=today)
        
        return songoftheday
