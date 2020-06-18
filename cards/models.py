from django.db import models
from django.contrib.auth.models import User


class Cards(models.Model):
    card_owner = models.ForeignKey(User, related_name="card_sets", on_delete=models.CASCADE, null=True)
    card_type = models.CharField(max_length=10)