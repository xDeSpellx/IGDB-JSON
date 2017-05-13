import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):
    GameGenre = django_filters.CharFilter(
        name='GameGenre__GenreTitle',
    )

    GamePlatform = django_filters.CharFilter(
        name='GamePlatform__PlatformName',
    )

    GamePublisher = django_filters.CharFilter(
        name='GamePublisher__PublisherName',
    )

    DateFrom =  django_filters.DateTimeFilter(name="GameReleaseDate",lookup_expr='gte')
    DateTo =  django_filters.DateTimeFilter(name="GameReleaseDate",lookup_expr='lte')

    PriceFrom =  django_filters.NumberFilter(name="GamePrice",lookup_expr='gte')
    PriceTo = django_filters.NumberFilter(name="GamePrice", lookup_expr='lte')

    class Meta:
        model = Game
        fields = ('GameTitle',)



