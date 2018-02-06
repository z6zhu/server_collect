# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

class DevopsRegister(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    passwd = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'devops_register'

class ClientInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'client_info'
    
class UpdateTestServer(models.Model):
    update_people = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    sys_variety = models.CharField(max_length=255)
    update_time = models.CharField(max_length=255)
    online_offline = models.CharField(max_length=255)
    except_info = models.CharField(max_length=5000)
 
    class Meta:
        managed = False
        db_table = 'update_test_server'
#         
        
# class UpdateTestServer(models.Model):
#     update_people = models.CharField(max_length=255)
#     server = models.CharField(max_length=255)
#     module = models.CharField(max_length=255)
#     sys_variety = models.CharField(max_length=255)
#     update_time = models.CharField(max_length=255)
#     except_info = models.CharField(max_length=1000)
#     online_offline = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'update_test_server'
        
class TestServer(models.Model):
    instance_id = models.CharField(db_column='instance_ID', unique=True, max_length=255)  # Field name made lowercase.
    instance_name = models.CharField(max_length=255)
    out_net = models.CharField(max_length=255)
    inner_net = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sys = models.CharField(db_column='SYS', max_length=255)  # Field name made lowercase.
    deadtime = models.CharField(max_length=255)
    project = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'test_server'
        
class OnlineServer(models.Model):
    instance_id = models.CharField(db_column='instance_ID', unique=True, max_length=255)  # Field name made lowercase.
    instance_name = models.CharField(max_length=255)
    out_net = models.CharField(max_length=255)
    inner_net = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    createtime = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    sys = models.CharField(db_column='SYS', max_length=255)  # Field name made lowercase.
    port = models.CharField(max_length=255)
    deadtime = models.CharField(max_length=255)
    bandwidth = models.CharField(max_length=255)
    project = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'online_server'
        
# zcell node 


class ModuleDetail(models.Model):
    module = models.CharField(max_length=255, blank=True, null=True)
    module_version = models.CharField(max_length=255, blank=True, null=True)
    module_date = models.CharField(max_length=255, blank=True, null=True)
    module_update = models.CharField(max_length=255, blank=True, null=True)
    additional = models.CharField(max_length=255, blank=True, null=True)
    module_in = models.CharField(max_length=255, blank=True, null=True)
    company_id = models.CharField(max_length=255)
 

    class Meta:
        managed = False
        db_table = 'module_detail'

class ZcellModule(models.Model):
    zone = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    server_ip = models.CharField(max_length=255)
    server_name = models.CharField(max_length=255)
    node = models.CharField(max_length=255)
    module_name = models.CharField(max_length=255)
    port = models.CharField(max_length=255)
    portv = models.CharField(max_length=255)
    passwd=models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'zcell_module'


# class ModuleDetail(models.Model):
#     module = models.CharField(primary_key=True, max_length=255)
#     module_version = models.CharField(max_length=255, blank=True, null=True)
#     module_date = models.CharField(max_length=255, blank=True, null=True)
#     module_update = models.CharField(max_length=255, blank=True, null=True)
#     additional = models.CharField(max_length=255, blank=True, null=True)
#     module_in = models.CharField(max_length=255)
#     
# 
#     class Meta:
#         managed = False
#         db_table = 'module_detail'
# 
# class ZcellModule(models.Model):
#     zone = models.CharField(max_length=255)
#     company_id = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     server_ip = models.CharField(max_length=255)
#     server_name = models.CharField(max_length=255)
#     node = models.CharField(max_length=255)
#     module_name = models.ForeignKey('ModuleDetail', models.DO_NOTHING, db_column='module_name')
#     port = models.CharField(max_length=255)
#     portv = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'zcell_module'
# 
#         

        


