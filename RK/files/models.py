from django.db import models
from django.utils import timezone


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class File(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=5)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

