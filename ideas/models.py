from django.db import models


# Create your models here.
class Idea(models.Model):
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    # TODO: Try different field types and play around with them
    # BooleanField
    # CharField
    # EmailField
    # IntegerField
