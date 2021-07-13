from django.db import models

class Pet(models.Model):
    # Note choices here is a list of tuples which are data value and display value
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField()
    submission_date = models.DateTimeField()
    vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)