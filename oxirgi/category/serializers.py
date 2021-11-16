from rest_framework.fields import CurrentUserDefault
from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    # author = serializers.SerializerMethodField('get_user')

    class Meta:
        model = Category
        fields = '__all__'


# funksiya uchun userni to'g'ridan to'g'ri bog'lash
class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['author', 'editor']

    # # viewda funksiya uchun
    # def create(self, validated_data, user):
    #     obj = Category.objects.create(author=user, **validated_data)
    #     return obj


class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['author', 'editor']