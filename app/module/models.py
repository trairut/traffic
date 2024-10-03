from django.db import models
from django.utils.timezone import now

# Create your models here.

class focus(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class group(models.Model):
    name = models.CharField(max_length=50)
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class location(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=200, blank=True)
    group = models.ForeignKey(group, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=20)
    longitude = models.FloatField(max_length=20)

    def __str__(self):
        return self.name

class statistics(models.Model):  
    temperature = models.FloatField(max_length=20)
    pm = models.FloatField(max_length=20)
    rainfall = models.FloatField(max_length=20)
    date = models.DateTimeField()

    # def __str__(self):
    #     return self.date

class location_statistics(models.Model):
    namelocation = models.ForeignKey(location, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=255)
    speedover = models.IntegerField(max_length=255)
    average_speed = models.IntegerField(max_length=255)



    # def __str__(self):
    #     return self.namelocation