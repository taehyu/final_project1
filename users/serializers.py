from rest_framework import serializers
from django.contrib.auth.models import User
from cards.serializers import CardSerializer
from contents.serializers import ContentSerializer


class UserSerializer(serializers.ModelSerializer):
    card = CardSerializer(many=True, read_only=True, source='card_sets')
    content = ContentSerializer(many=True, read_only=True, source='content_sets')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'card', 'content', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
