from django.shortcuts import render
from .models import Game, Platform, Genre, Publisher

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, request
from .serializers import GameSerializer,GenreSerializer,PlatformSerializer,PublisherSerializer
from rest_framework import filters
from rest_framework import generics
from .filters import GameFilter
import django_filters
from rest_framework.generics import ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView

#RETRIEVE
class GameList(ListAPIView):
    queryset = Game.objects.all()
    serializer_class=GameSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('GameTitle',)
    filter_class = GameFilter
    ordering_fields= ('GameTitle','GameRating','GameReleaseDate')

class GameDetail(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

#UPDATE
class GameUpdate(UpdateAPIView,RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

#DELETE
class GameDestroy(DestroyAPIView,RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

#CREATE
class GameCreate(CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated]

class GenreList(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformList(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


def home_page(request):
    latestgames = Game.objects.order_by('-GameReleaseDate')[:8]
    topGames = Game.objects.order_by('-GameRating')[:8]
    rndGames = Game.objects.all().order_by('?')[:8]
    return render(request, 'home.html', {'latestgames':latestgames,'topGames':topGames,'rndGames':rndGames})

def genres(request):
    genres = Genre.objects.all()
    return render(request, 'genres.html', {'genres':genres})

def platforms(request):
    platforms = Platform.objects.all()
    return render(request, 'platforms.html', {'platforms':platforms})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'publishers.html', {'publishers':publishers})

def search(request):
    platforms = Platform.objects.all()
    genres = Genre.objects.all()
    return render(request,'search.html',{'platforms':platforms,'genres':genres})


def ajax_search(request):
    if request.method == "GET":
        search_text = request.GET['search_text']
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
            games = Game.objects.filter(GameTitle__contains = search_text)
        else:
            games = Game.objects.all()

        return render(request, 'ajax_search.html', {'games':games})


def genresList(request,genre):
    genreOBJ = Genre.objects.get(GenreTitle = genre)
    games = Game.objects.filter(GameGenre__GenreTitle=genre)
    return render(request,'genreCategory.html',{'games':games,'genreOBJ':genreOBJ})

def publisherList(request,publisher):
    publisherOBJ = Publisher.objects.get(PublisherName=publisher)
    games = Game.objects.filter(GamePublisher__PublisherName=publisher)
    return render(request, 'publisherList.html', {'games': games,'publisherOBJ':publisherOBJ})

def platformList(request,platform):
    platformOBJ = Platform.objects.get(PlatformName = platform)
    games = Game.objects.filter(GamePlatform__PlatformName=platform)
    return render(request, 'platformList.html', {'games': games,'platformOBJ':platformOBJ})

def gameList(request,game):
    gameOBJ = Game.objects.get(GameTitle=game)
    return render(request, 'game.html',{'gameOBJ':gameOBJ} )