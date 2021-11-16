from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from accounts.models import CustomUser


class CustomUserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class CustomUserCreateSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'password', 'groups')

    def validate(self, attr):
        validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        for group_data in groups_data:
            # Group.objects.create(user=user, **group_data)
            user.groups.add(group_data)
        user.save()
        return user


class AdminCreateSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'password', 'groups')

    def validate(self, attr):
        validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = CustomUser.objects.create_superuser(**validated_data)
        user.set_password(validated_data['password'])
        for group_data in groups_data:
            # Group.objects.create(user=user, **group_data)
            user.groups.add(group_data)
        user.save()
        return user


class GroupCreateSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
