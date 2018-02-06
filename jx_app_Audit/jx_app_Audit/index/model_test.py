# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class UpdateTestServer(models.Model):
    update_people = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    sys_variety = models.CharField(max_length=255)
    update_time = models.CharField(max_length=255)
    except_info = models.CharField(max_length=1000)
    online_offline = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'update_test_server'
