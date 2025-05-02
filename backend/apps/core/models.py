"""Core app models."""
from django.db import models

# Add your models here
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.breed}"

    class Meta:
        verbose_name = "Cat"
        verbose_name_plural = "Cats"