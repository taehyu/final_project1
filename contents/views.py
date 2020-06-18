from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contents.serializers import ContentSerializer
from contents.permissions import IsOwnerOrReadOnly
from contents.models import Contents

from django.contrib.auth.models import User


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Contents.objects.all()
    serializer_class = ContentSerializer

    def get_permissions(self):

        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

