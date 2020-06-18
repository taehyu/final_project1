from rest_framework import serializers
from cards.models import Cards
from django.contrib.auth.models import User


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cards
        fields = ('card_owner', 'card_type',)
