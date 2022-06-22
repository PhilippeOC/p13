from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
