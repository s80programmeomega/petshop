from django.db import models
from django.contrib.auth.models import AbstractUser

from petshop.utils import DEFAULT_SIZE, get_uuid


class User(AbstractUser):
    id = models.CharField(primary_key=True, default=get_uuid, max_length=DEFAULT_SIZE,editable=False)
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='accounts/profile_pics')

    # when loggin in, we want to return the user's email instead of username
    USERNAME_FIELD = "email"
    # when creating a new user, we want to use the email field instead of username
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    
