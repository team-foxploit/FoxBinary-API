from foxbinaryapi.models import TickHistory, BlogPost
from rest_framework import serializers

# TickHistory serializer
class TickHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TickHistory
        fields = '__all__'

# BlogPost serilizer
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
