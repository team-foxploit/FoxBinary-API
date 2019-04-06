from foxbinaryapi.models import TickHistory
from rest_framework import viewsets, permissions
from .serializers import TickHistorySerializer

# Tick History Serializer
class TickHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = TickHistory.objects.all()
    serializer_class = TickHistorySerializer