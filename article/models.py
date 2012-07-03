# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
class SimpleNews(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название для поисковика')) # заголовок для поисковика
    description = models.CharField(max_length = 255, blank=True, verbose_name= (u'Описание для поисковика')) # описание для поисковиков
    header = models.TextField(verbose_name= (u'Название для людей')) # заголовок для новости
    newsimages = models.ImageField(upload_to="news", verbose_name= (u'рисунок')) # рисунок для новости
    briefcontent = models.TextField(verbose_name= (u'краткое содержание')) # краткое содержимое новости
    fullcontent = models.TextField(verbose_name= (u'подробное содержание')) #  подробное содержимое новости
    contentdata = models.DateField(verbose_name= (u'дата публикации')) #  дата публикации
    CategoryKey = models.ForeignKey('SimpleNewsCategory')

    def __unicode__(self):
        result = self.title + str(self.contentdata)
        return result

class SimpleNewsCategory(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название для поисковика')) # заголовок для поисковика
    description = models.CharField(max_length = 255, blank=True, verbose_name= (u'Описание для поисковика')) # описание для поисковиков
    header = models.TextField(verbose_name= (u'Название для людей')) # заголовок для новости
    newsimages = models.ImageField(upload_to="news", verbose_name= (u'рисунок')) # рисунок для новости
    briefcontent = models.TextField(verbose_name= (u'краткое содержание')) # краткое содержимое новости
    fullcontent = models.TextField(verbose_name= (u'подробное содержание')) #  подробное содержимое новости
    contentdata = models.DateField(verbose_name= (u'дата публикации')) #  дата публикации
    CategoryKey = models.ForeignKey('SimpleNewsCategory')

    def __unicode__(self):
        result = self.title + str(self.contentdata)
        return result