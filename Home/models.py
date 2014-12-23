from django.db import models

# Create your models here.
class Property(models.Model):
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.ForeignKey('Size')
    proximity_to_volcanoe = models.IntegerField()
    school_rating = models.IntegerField()
    distance_to_bar = models.FloatField()
    image = models.URLField()
    home_type = models.CharField(max_length=100)
    distance_to_public_transit = models.FloatField()

class Size(models.Model):
	num_bedrooms = models.IntegerField()
	num_bathrooms = models.IntegerField()
	sq_ft = models.IntegerField()
	lot_sq_ft = models.IntegerField()