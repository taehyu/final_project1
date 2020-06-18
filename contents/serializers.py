from rest_framework import serializers
from contents.models import Contents

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contents
        fields = ('content_owner', 'content_type',)