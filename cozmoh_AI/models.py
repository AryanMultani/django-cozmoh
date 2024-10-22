from django.db import models


class TextGeneration(models.Model):
  industry=models.CharField(max_length=255)
  page_type=models.CharField(max_length=255)
  page_section=models.CharField(max_length=255)

  def __str__(self):
    return self.industry + " " + self.page_type + " " + self.page_section


  class Meta:
    verbose_name="In Progres"
    # verbose_plural_name="Cozmoh AI"