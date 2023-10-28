from django.db import models


class Feedback(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=40)
    emailAlt = models.EmailField(max_length=40, blank=True)
    country = models.CharField(max_length=20, blank=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.firstname) + ' ' + str(self.lastname)


class Buyer(models.Model):
    name = models.CharField(max_length=40, default='')
    email = models.EmailField(max_length=40, default='')
    address = models.TextField(max_length=50, default='')
    shirt_size = models.CharField(max_length=25, default='')
    credit_card_number = models.CharField(max_length=16, default='')
    valid_date = models.CharField(max_length=5, default='')
    cvv = models.CharField(max_length=3, default='')

    def __str__(self):
        return self.name
