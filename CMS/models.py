from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FileInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=300)
    userId = models.CharField(max_length=100)
    addTime = models.CharField(max_length=50)
    hits = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)

class UserInfo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userName = models.CharField(max_length=100)
    userUrl = models.URLField()
    userAvaUrl = models.URLField()
    hits = models.IntegerField(default=0)

class SearchInfo(models.Model):
    id = models.AutoField(primary_key=True)
    searchText = models.CharField(max_length=50)
    searchCount = models.IntegerField(default=0)
    mSearchCount = models.IntegerField(default=0)
    searchTime = models.CharField(max_length=50, default='0')

'''class TagInfo(models.Model):
    id = models.AutoField(primary_key=True)
    tagName = models.CharField(max_length=50)
    fileId = models.IntegerField()'''
