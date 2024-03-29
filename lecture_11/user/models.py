from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    bio = models.CharField(max_length=255, null=False, default='')
    avatar = models.ImageField(upload_to='user/', null=True, max_length=2000)
    resume = models.FileField(upload_to='user/', null=True, max_length=2000)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.id} {self.owner.email}'





