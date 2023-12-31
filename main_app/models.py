from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

# Create your models here.
class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
  species = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  wing_span = models.DecimalField(max_digits=3, decimal_places=1, default=1)
  habitat = models.CharField(max_length=100)
  lifespan = models.IntegerField()
  toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.species
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})


class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
  # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']

