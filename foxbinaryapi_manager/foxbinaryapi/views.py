from django.shortcuts import render
from rest_framework import viewsets
from foxbinaryapi.models import TickHistory
from foxbinaryapi.serializers import TickHistorySerializer

# Create your views here.
class TickHistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tick history to be viewed or edited.
    """
    queryset = TickHistory.objects.all().order_by('-date_joined')
    serializer_class = TickHistorySerializer