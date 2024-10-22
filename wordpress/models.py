from django.db import models


class Site(models.Model):
  site_url=models.CharField(max_length=255)
  username=models.CharField(max_length=255)
  password=models.CharField(max_length=255)
  plugin=models.TextField()

  def __str__(self):
    return self.site_url




