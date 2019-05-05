from foxbinaryapi.models import TickHistory, BlogPost, APIToken
from rest_framework import viewsets, permissions
from .serializers import TickHistorySerializer, BlogPostSerializer, APITokenSerializer
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

class APITokenViewSet(viewsets.ModelViewSet):
    ermission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = APITokenSerializer

    def get_queryset(self):
        return self.request.user.api_tokens.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)