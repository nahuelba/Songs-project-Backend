from rest_framework import serializers
from songoftheday.models import InterpreterModel, LinksSongsModel, SongModel


class interpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterpreterModel
        fields = ['interpreter_name', 'interpreter_image']

class LinkSongsSerializer(serializers.ModelSerializer):
    interpreters = interpreterSerializer(many=True)

    class Meta:
        model  = LinksSongsModel
        exclude = ['id', 'song_title']

class SongSerializer(serializers.ModelSerializer):
    composer= interpreterSerializer()
    links = LinkSongsSerializer(many=True)
    


    class Meta:
        model = SongModel
        fields=  '__all__'



