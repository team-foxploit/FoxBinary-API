from foxbinaryapi.models import TickHistory, BlogPost, APIToken
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

# APIToken Serializer
class APITokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIToken
        fields = '__all__'
