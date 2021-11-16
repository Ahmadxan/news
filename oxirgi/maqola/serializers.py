from .models import *
from rest_framework import serializers


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['author', 'editor']


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['author', 'editor']


