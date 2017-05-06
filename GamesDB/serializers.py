from rest_framework import serializers
from .models import Game,Publisher,Genre,Platform
import django_filters

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publisher
        fields = ('PublisherName',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Genre
        fields=('GenreTitle',)

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platform
        fields=('PlatformName',)

class GameSerializer(serializers.ModelSerializer):
    GamePublisher = PublisherSerializer(many=False)
    GameGenre = GenreSerializer(many=True)
    GamePlatform = PlatformSerializer(many=True)

    class Meta:
        model = Game

        fields = ('GameTitle','GamePublisher','GameGenre','GameReleaseDate',
                 'GamePhoto','GamePrice','GameDescription','GameVideoURL','GameRating',
                'GamePlatform','GameReview')