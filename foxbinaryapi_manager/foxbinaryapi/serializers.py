from foxbinaryapi.models import TickHistory
from rest_framework import serializers

# TickHistory seralizer
class TickHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TickHistory
        fields = '__all__'
