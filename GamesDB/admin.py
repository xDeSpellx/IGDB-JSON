from django.contrib import admin
from .models import Game, Publisher, Genre, Platform
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import models

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Game)
admin.site.register(Publisher)
admin.site.register(Genre)
admin.site.register(Platform)

#Counters for each object
Game._meta.verbose_name_plural = "Games (%s) " % Game.objects.all().count()
Publisher._meta.verbose_name_plural = "Publishers (%s) " % Publisher.objects.all().count()
Genre._meta.verbose_name_plural = "Genres (%s) " % Genre.objects.all().count()
Platform._meta.verbose_name_plural = "Platforms (%s) " % Platform.objects.all().count()

