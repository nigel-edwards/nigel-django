from django.db import models

class Pet(models.Model):
    # Note choices here is a list of tuples which are data value and display value
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(maxlength=100)
    submitter = models.CharField(maxlength=100)
    species = models.CharField(maxlength=30)
    breed = models.CharField(maxlength=30, blank=True)
    description = models.TextField()
    sex = models.CharField(maxlength=1, choices=SEX_CHOICES, blank=True)
    age = models.IntegerField()
    submission_date = models.TimeDateField()
    vaccinations = models.ManyToManyField('Vaccine', blank = True)

class Vaccine(models.Model):
    name = models.CharField(maxlength=50)