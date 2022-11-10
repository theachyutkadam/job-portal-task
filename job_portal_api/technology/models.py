from django.db import models

# Create your models here.
class Technology(models.Model):
  name = models.CharField(max_length=60)
  description = models.TextField(max_length=500)
  is_active = models.BooleanField(default=True)

  def __str__(self):
    return self.name
