from django.db import models
from course.models import Course

# Create your models here.
class Program(models.Model):
  name = models.CharField(max_length=25)
  description = models.TextField(max_length=500)
  course = models.ForeignKey(Course, on_delete = models.CASCADE, blank = False)
  detail_overview = models.TextField(max_length=500)
  cover_image = models.ImageField(upload_to='photos', null=True)
  banner_image = models.ImageField(upload_to='photos', null=True)
  is_active = models.BooleanField(default = True)
  learning_mode = models.CharField(max_length=25)
  start_date = models.DateField(max_length=25)
  end_date = models.DateField(max_length=25)
  training_option = models.CharField(max_length=25)
  type = models.CharField(max_length=25)
  seats = models.IntegerField(null=True)
  feature = models.CharField(max_length=25)
  requirement = models.CharField(max_length=25)
  eligitbility = models.CharField(max_length=25)
  tools_coverd = models.CharField(max_length=25)
  skill = models.CharField(max_length=25)
  is_free_course = models.BooleanField(default = False, blank = True)
  meta_keywords = models.TextField(max_length=500)
  meta_description = models.TextField(max_length=500)

  def __str__(self):
    return self.name
