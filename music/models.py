# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    name= models.CharField(max_length=200)
    image = models.ImageField(upload_to='album_img/')
    genre = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Song(models.Model):
    album = models.ForeignKey(Album)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)


    def __str__(self):
        return self.name
