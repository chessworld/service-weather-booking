from django.db import models


class User(models.Model):
    name                = models.CharField(max_length=100, null=True, default=None)
    completed_tutorial  = models.BooleanField(default=False)
