from django.db import models

# Create your models here.
class Resume(models.Model):
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  gender = models.CharField(max_length=25)
  contact = models.CharField(max_length=25)
  github_link = models.URLField()
  twitter_link = models.URLField()
  avatar = models.ImageField(max_length=None, blank=True)

  def __str__(self):
    return self.first_name
