from django.db import models

# Create your models here.
class MerchType(models.Model):
    name = models.CharField(max_length = 200)
    comment = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/artist', blank = True, null = True)
    bias = models.BooleanField(blank = True, null = True)
    comment = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    
class Group(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/group', blank = True, null = True)
    artist = models.ManyToManyField(Artist, blank = True)
    comment = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name
    
class Event(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/event', blank = True, null = True)
    group = models.ManyToManyField(Group, blank = True)
    version = models.CharField(max_length = 200, null = True, blank = True)
    comment = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

class Merch(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/merch', blank = True, null = True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL,blank = True, null = True)
    group = models.ManyToManyField(Group, blank = True)
    artist = models.ManyToManyField(Artist, blank = True)
    merchType = models.ForeignKey(MerchType, on_delete=models.SET_NULL,blank = True, null = True)
    own = models.BooleanField(blank = True, null = True)
    quantity = models.PositiveIntegerField(blank = True, null = True)
    exchangeSale = models.BooleanField(blank = True, null = True)
    wishList = models.BooleanField(blank = True, null = True)
    comment = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name


