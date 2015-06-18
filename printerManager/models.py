from django.db import models

# Create your models here.


class RegisterPrinter(models.Model):
    '''
    define the registered printer infor
    <id, code, name, location, password, speed>
    '''
    code = models.CharField(unique=True, max_length=100, default='0x000')
    name = models.CharField(max_length=20, default='test')
    location = models.CharField(max_length=100, default='localhost')
    password = models.CharField(max_length=100, default='passw0rd')
    speed = models.FloatField(default=10)
    cost = models.FloatField(default=0.1)
    star = models.FloatField(default=3)


class State(models.Model):
    '''
    The informtion of printers which added in the cloud platform
    '''
    code = models.CharField(unique=True, max_length=100, default='0x000')
    printerStates = models.CharField(max_length=4, default='off')
    remainJobsNum = models.IntegerField(default=-1)
    currentJobPages = models.IntegerField(default=-1)
    currentJobName = models.CharField(max_length=100, default='testJob.pdf')
