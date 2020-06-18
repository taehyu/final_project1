from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cards.permissions import IsOwnerOrReadOnly
from cards.serializers import CardSerializer
from cards.models import Cards


class CardViewSet(viewsets.ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

    def get_permissions(self):
        if self.action in ['partial_update', 'update', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]