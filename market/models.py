from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    pages = models.IntegerField()
    description = models.CharField(max_length=100)
    store_location = models.CharField(max_length=100)
