from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  species = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  wing_span = models.DecimalField(max_digits=3, decimal_places=1, default=1)
  habitat = models.CharField(max_length=100)
  lifespan = models.IntegerField()

  def __str__(self):
    return self.species
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})
