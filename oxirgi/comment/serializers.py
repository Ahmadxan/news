from .models import *
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['user']


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["user"]
