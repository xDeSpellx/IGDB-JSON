from django.db import models
from django.utils import timezone

class Genre(models.Model):
    GenreTitle = models.CharField(max_length=30,verbose_name = 'Title')
    GenreDescription = models.TextField(max_length=500,verbose_name = 'Description')
    GenreImage = models.ImageField(null=True, verbose_name='Image')

    def __str__(self):
        return self.GenreTitle

class Platform(models.Model):
    PlatformName = models.CharField(max_length=30,verbose_name = 'Title')
    PlatformDescription = models.TextField(max_length=500,verbose_name = 'Description')
    PlatformImage = models.ImageField(null=True, verbose_name='Image')

    def __str__(self):
        return self.PlatformName

class Game(models.Model):
   GameRatingChoices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
    )
   GameTitle = models.CharField(max_length=50,verbose_name = 'Title')
   GameDescription = models.TextField(max_length=99999,verbose_name = 'Description')
   GameGenre = models.ManyToManyField(Genre,verbose_name='Genre')
   GamePlatform = models.ManyToManyField(Platform,verbose_name='Platform')
   GameReleaseDate = models.DateField(default=timezone.now,verbose_name = 'Release Date')
   GamePublisher = models.ForeignKey('Publisher', verbose_name = 'Publisher',default=1)
   GamePhoto = models.ImageField(null=True,verbose_name = 'Image')
   GameVideoURL = models.CharField(max_length=100,verbose_name = 'Video URL')
   GameReview = models.TextField(max_length=99999,verbose_name = 'Review')
   GameRating = models.CharField(max_length=3,choices=GameRatingChoices,default='1',verbose_name = 'Rating')
   GamePrice = models.FloatField(verbose_name='Price')

   def __str__(self):
       return self.GameTitle

   class Meta:
       ordering = ('GameTitle',)

class Publisher(models.Model):
    PublisherName = models.CharField(max_length=30,verbose_name = 'Name')
    PublisherCEO =  models.CharField(max_length=30,verbose_name = 'CEO')
    PublisherFoundDate = models.DateField(default=timezone.now,verbose_name = 'Founded')
    PublisherEmployeeNumber = models.IntegerField(verbose_name='Number of employees')
    PublisherWebsite = models.CharField(max_length=30,verbose_name = 'Website')
    PublisherLogo = models.ImageField(null=True,verbose_name = 'Image')

    def __str__(self):
        return self.PublisherName
