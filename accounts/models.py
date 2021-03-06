from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Profile")
    description = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.user.username
        