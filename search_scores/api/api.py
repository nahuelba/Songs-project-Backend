from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from search_scores.models import ScoresModel, EditorialModel
from search_scores.api.serializers import ScoresSerializer, EditorialSerializer



class ScoresListAPIView(ListAPIView):

    serializer_class = ScoresSerializer

    def get_queryset(self):
        return ScoresModel.objects.all()
    
class ArtistListAPIView(ListAPIView):

    serializer_class = EditorialSerializer

    def get_queryset(self):
        return EditorialModel.objects.all()