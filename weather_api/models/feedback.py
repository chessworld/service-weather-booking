from django.db import models
import uuid

class Feedback(models.Model):
    # Generate a UUID for id
    id                  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating              = models.IntegerField()
    comment             = models.CharField(max_length=500, null=True, default=None)