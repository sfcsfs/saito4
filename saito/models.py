from sre_constants import CATEGORY
from django.db import models

# Create your models here.

class  add_pension(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    kinngaku  = models.IntegerField(blank=True, null=True)
        
    def __str__(self):
        return self.title