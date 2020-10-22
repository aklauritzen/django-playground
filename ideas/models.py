from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Idea(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=220)
    content = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    # TODO: Try different field types and play around with them
    # BooleanField
    # CharField
    # EmailField
    # IntegerField
