from django.db import models
from django.contrib.auth.models import User


class Contents(models.Model):
    content_owner = models.ForeignKey(User, related_name="content_sets", on_delete=models.CASCADE, null=True)
    content_type = models.CharField(max_length=10)