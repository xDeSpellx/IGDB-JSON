from rest_framework import serializers
from .models import Game,Publisher,Genre,Platform
import django_filters

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields= '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platform
        fields='__all__'

class GameSerializer(serializers.ModelSerializer):
    GamePublisher = PublisherSerializer(many=False,read_only=True)
    GameGenre = GenreSerializer(many=True,read_only=True)
    GamePlatform = PlatformSerializer(many=True,read_only=True)



    class Meta:
        model = Game
        fields = '__all__'

