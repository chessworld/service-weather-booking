from django.db import models
import uuid


class User(models.Model):
    # Generate a UUID for id
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name                = models.CharField(max_length=100, null=True, default=None)
    completed_tutorial  = models.BooleanField(default=False)
