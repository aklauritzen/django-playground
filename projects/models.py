from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=220)
    teaser = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    # Image
    # Language tag