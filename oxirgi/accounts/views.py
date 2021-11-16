from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import CustomUser
from accounts.serializers import CustomUserListSerializer, CustomUserCreateSerializer, AdminCreateSerializer, \
    GroupCreateSerializer


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserListSerializer


class CustomUserCreateView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = CustomUser,
    serializer_class = CustomUserCreateSerializer


class AdminCreateListView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AdminCreateSerializer


class AdminApiView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AdminCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GroupCreateView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer
