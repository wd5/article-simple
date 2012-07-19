# -*- coding: UTF-8 -*-
from django.db import models

# ************************************* NEWS ***********************************************************

class SecNew(models.Model):
    # новости, акции, новинки и т.п.
    title = models.CharField(max_length = 300, verbose_name= (u'Название')) # заголовок для поисковика
    newsimages = models.ImageField(upload_to="news", verbose_name= (u'Миниатюра')) # рисунок для новости
    briefcontent = models.TextField(verbose_name= (u'Текст')) # краткое содержимое новости
    timestart = models.DateField(verbose_name= (u'дата публикации')) #  дата публикации
    timeend = models.DateField(verbose_name= (u'дата отмены публикации')) #  дата публикации
    CategoryKey = models.ForeignKey('SecNewCat')

    def __unicode__(self):
        result = self.title
        return result

class SecNewCat(models.Model):
    # классификатор для новостного материала
    title = models.CharField(max_length = 300, verbose_name= (u'Название категории новостей')) # заголовок для поисковика
    CategoryKey = models.ForeignKey('SecNewCat')

    def __unicode__(self):
        result = self.title
        return result

# ************************************* ARTICLE ***********************************************************

class SingleArticle(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название для поисковика')) # заголовок для поисковика
    description = models.CharField(max_length = 255, blank=True, verbose_name= (u'Описание для поисковика')) # описание для поисковиков
    header = models.TextField(verbose_name= (u'Название для людей')) # заголовок для новости
    newsimages = models.ImageField(upload_to="news", verbose_name= (u'рисунок')) # рисунок для новости
    briefcontent = models.TextField(verbose_name= (u'краткое содержание')) # краткое содержимое новости
    fullcontent = models.TextField(verbose_name= (u'подробное содержание')) #  подробное содержимое новости
    contentdata = models.DateField(verbose_name= (u'дата публикации')) #  дата публикации
    CategoryKey = models.ForeignKey('SingleArticleCategory')

    def __unicode__(self):
        result = self.title + str(self.contentdata)
        return result

class SingleArticleCategory(models.Model):
    title = models.CharField(max_length = 300, verbose_name= (u'Название для поисковика')) # заголовок для поисковика
    description = models.CharField(max_length = 255, blank=True, verbose_name= (u'Описание для поисковика')) # описание для поисковиков
    header = models.TextField(verbose_name= (u'Название для людей')) # заголовок для новости
    newsimages = models.ImageField(upload_to="news", verbose_name= (u'рисунок')) # рисунок для новости
    briefcontent = models.TextField(verbose_name= (u'краткое содержание')) # краткое содержимое новости
    fullcontent = models.TextField(verbose_name= (u'подробное содержание')) #  подробное содержимое новости
    contentdata = models.DateField(verbose_name= (u'дата публикации')) #  дата публикации
    CategoryKey = models.ForeignKey('SingleArticleCategory')

    def __unicode__(self):
        result = self.title + str(self.contentdata)
        return result

# ************************************* LINKs Catalog ***********************************************************

# ************************************* Tools Catalog **********************************************************

# ************************************* Photo Portfolio ***********************************************************