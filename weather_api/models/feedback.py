import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Feedback(models.Model):
    # Generate a UUID for id
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating              = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1"),
            MaxValueValidator(5, message="Rating must be at most 5")
        ]
    )
    comment             = models.CharField(max_length=500, null=True, default=None)
