
from __future__ import unicode_literals

from django.db import models

 
class IndexBook(models.Model):
    title = models.CharField(max_length=255)
 
    class Meta:
        managed = False
        db_table = 'index_book'
 
class IndexAuthor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
 
    class Meta:
        managed = False
        db_table = 'index_author'
 
class IndexBookAuthor(models.Model):
    book = models.ForeignKey('IndexBook', models.DO_NOTHING)
    author = models.ForeignKey('IndexAuthor', models.DO_NOTHING)
 
    class Meta:
        managed = False
        db_table = 'index_book_author'
         
