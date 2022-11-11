from django.db import models
from technology.models import Technology

# Create your models here.
class Course(models.Model):
  name = models.CharField(max_length=25)
  slug = models.CharField(max_length=25)
  description = models.TextField(max_length=500, blank=True)
  technology_id = models.ForeignKey(Technology, on_delete=models.CASCADE)
  icon = models.CharField(max_length=25)
  image = models.ImageField(max_length=None, blank=True)
  meta_keywords = models.TextField(max_length=500, blank=True)
  meta_description = models.TextField(max_length=500, blank=True)
  is_active = models.BooleanField(default=True)
  banner = models.BooleanField(default=True)

  def __str__(self):
    return self.name
