from django.db import models

# Create your models here.

class Currency(models.Model):
  code = models.CharField(max_length=3)
  description = models.CharField(max_length=80)
  rate = models.DecimalField(max_digits=12, decimal_places=6)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f'{self.code} - {self.description} - {self.rate} - Last Updated: {self.updated_at}' 

  
