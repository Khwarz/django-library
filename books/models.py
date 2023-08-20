from django.db import models


class Book(models.Model):
    title: models.CharField = models.CharField(max_length=255)
    subtitle: models.CharField = models.CharField(max_length=255)
    author: models.CharField = models.CharField(max_length=100)
    isbn: models.CharField = models.CharField(max_length=13)

    def __str__(self):
        return self.title
