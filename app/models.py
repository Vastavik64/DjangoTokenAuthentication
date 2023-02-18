from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class user(models.Model):
    '''
    This class creates a model user in django database with the fields defined
    '''
    id = models.AutoField(primary_key = True, auto_created=True)
    name = models.TextField()
    birthdate = models.DateField()
    gender = models.TextField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    '''
    This automatically generates token when a user is created
    '''
    if created:
        Token.objects.create(user=instance)