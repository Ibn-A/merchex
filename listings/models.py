from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900),MaxValueValidator(2023)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    
class Listing(models.Model):
    title = models.fields.CharField(max_length=100)