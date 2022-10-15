from django.db import models

# Create your models here.
class GPXFile(models.Model):
    newfile = models.FileField(upload_to='media/gpx')