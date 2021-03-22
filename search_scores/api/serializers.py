from rest_framework import serializers
from search_scores.models import EditorialModel, ScoresModel


class ScoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoresModel
        exclude = ['created']

class EditorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = EditorialModel
        fields= '__all__'
