from django.db import models
from resume.models import Resume

# Create your models here.
class Experiance(models.Model):
  role = models.CharField(max_length=25)
  company_name = models.CharField(max_length=25)
  start_date = models.DateField()
  end_date = models.DateField()
  resume_id = models.ForeignKey(Resume, on_delete=models.CASCADE)
  description = models.TextField(max_length=500, blank=True)
  banner = models.ImageField(max_length=None, blank=True)

  def __str__(self):
    return self.role
