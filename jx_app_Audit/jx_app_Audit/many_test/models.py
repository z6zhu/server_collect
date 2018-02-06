# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Author(models.Model):    
    first_name = models.CharField(max_length=30)    
    last_name = models.CharField(max_length=40)    
    email = models.EmailField()    
        
class Book(models.Model):    
    title = models.CharField(max_length=200)    
    authors = models.ManyToManyField(Author) 
