from django.db import models
from django.urls import reverse

# Create your models here.
class Person(models.Model):
    """Model representing a Person register."""
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)

    class Meta:
        ordering = ['name']
    
    
    def get_absolute_url(self):
        return reverse('person-detail', args=[str(self.id)])
    

    def __str__(self):
        return self.name
