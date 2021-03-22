from rest_framework import serializers
from songoftheday.models import InterpreterModel, LinksSongsModel, SongModel


class interpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterpreterModel
        fields = '__all__'

class LinkSongsSerializer(serializers.ModelSerializer):
    class Meta:
        model  = LinksSongsModel
        fields= '__all__'

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongModel
        fields=  '__all__'



