from django.shortcuts import render
from rest_framework import viewsets
from foxbinaryapi.models import TickHistory, BlogPost
from foxbinaryapi.serializers import TickHistorySerializer, BlogPostSerializer

# Create your views here.
class TickHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tick history to be viewed or edited.
    """
    queryset = TickHistory.objects.all().order_by('-date_joined')
    serializer_class = TickHistorySerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog post to be viewed or edited.
    """
    queryset = BlogPost.objects.all().order_by('-date_joined')
    serializer_class = BlogPostSerializer
