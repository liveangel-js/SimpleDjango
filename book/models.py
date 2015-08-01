# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    qq  = models.CharField(max_length=20)

    def __unicode__(self):
        return u'%s' % self.name

#自定义query_set

class PythonManager(models.Manager):
    def get_query_set(self):
        return super(PythonManager, self).get_query_set().filter(title='software engineer')

#自定的manager 获取特定标题的书的数量
class BookManager(models.Manager):
    def get_book_count(self, keyword):
        return self.filter(title=keyword).count()

class Book(models.Model):
    title = models.CharField(max_length=50)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    objects = BookManager()
    python_objects = PythonManager()

    def __unicode__(self):
        return self.title

