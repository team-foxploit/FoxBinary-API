from foxbinaryapi.models import TickHistory, BlogPost
from rest_framework import viewsets, permissions
from .serializers import TickHistorySerializer, BlogPostSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Tick History Serializer
class TickHistoryViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = TickHistory.objects.all()
    serializer_class = TickHistorySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    @action(detail=True, methods=['get'], name='Review')
    def get(self, request, *args, **kwargs):
        print(request)
        return Response("LOL")