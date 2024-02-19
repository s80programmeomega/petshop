from django.db import models
from django.contrib.auth import get_user_model
from petshop.utils import DEFAULT_SIZE, get_uuid




class Specie(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="species",
        verbose_name="Added By",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE, related_name="breeds")
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="breeds",
        verbose_name="Added By",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="pets")
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE, related_name="photos")
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="pets_photos",
        verbose_name="Added By",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pet(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    name = models.CharField(max_length=255, unique=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="pets")
    age = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    owner = models.ForeignKey(
        "Owner", on_delete=models.SET_NULL, null=True, related_name="pets"
    )

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="pets",
        verbose_name="Added By",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OwnerPhoto(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="owners")
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE, related_name="photos")
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="owners_photos",
        verbose_name="Added By",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Owner(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=DEFAULT_SIZE,
        default=get_uuid,editable=False
    )
    name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        related_name="owners",
        verbose_name="Added By",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

