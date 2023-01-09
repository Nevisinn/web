from django.db import models

# Create your models here.
class Analytics(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d")

    class Meta:
        verbose_name = 'Специалист по информационной безопасности'
        verbose_name_plural = 'Специалист по информационной безопасности'

class Geography(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d")

    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'География'