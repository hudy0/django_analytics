from datetime import datetime

from django.db import models


class Customer(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
    ]

    name: str = models.CharField(max_length=50)
    gender: str = models.CharField(max_length=1, choices=GENDER_CHOICES, default=OTHER)
    age: int = models.PositiveSmallIntegerField()
    favorite_number: int = models.PositiveSmallIntegerField()
    created_at: datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.gender}"
