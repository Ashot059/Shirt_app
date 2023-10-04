from django.db import models


class Feedback(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    emailAlt = models.EmailField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    comment = models.TextField()


class Buyer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    shirt_size = models.CharField(max_length=10)
