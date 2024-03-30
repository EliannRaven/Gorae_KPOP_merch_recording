from django.db import models

# Create your models here.
class MerchType(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/artist', blank = True, null = True)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/group', blank = True, null = True)
    artist = models.ManyToManyField(Artist, blank = True)

    def __str__(self):
        return self.name
    
class Merch(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

