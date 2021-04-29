  
from .models import Newsapi
from rest_framework import serializers

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsapi
        fields = ['id','newstitle', 'source', 'content', 'url','favourite','category']
