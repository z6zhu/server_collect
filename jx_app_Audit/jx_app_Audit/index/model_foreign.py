from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'Person'
class Membership(models.Model):
    person = models.ForeignKey('Person', models.DO_NOTHING, db_column='person', blank=True, null=True)
    invite_reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Membership'



