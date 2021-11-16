from rest_framework import permissions, pagination, filters, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView
)
from maqola.pagenation import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


class UserListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]


class CategoryListView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'id']


class CategoryDetailView(RetrieveAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]


class CategoryCreateView(ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryUpdateView(RetrieveUpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoryUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class CategoryDeleteView(RetrieveDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]



# class CategoryListView(APIView):
#     pagination_classes = (CustomPagination,)
#
#     def get(self, request, *args, **kwargs):
#         categories = models.Category.objects.all()
#         serializer = serializers.CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#
# class CategoryDetailView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         try:
#             if kwargs.get('pk'):
#                 category = models.Category.objects.get(id=kwargs.get('pk'))
#                 serializer = serializers.CategorySerializer(category, many=False)
#                 return Response(serializer.data)
#         except Exception:
#             raise NotFound("Category not found!")
#
#
# class CategoryCreateView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def post(self, request):
#         serializer = serializers.CategoryCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             # serializer.save(author=self.request.user)
#             obj = serializer.create(serializer.data, request.user)
#         return Response(status=status.HTTP_201_CREATED)
#
#
# class CategoryUpdateView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def put(self, request, *args, **kwargs):
#         category = models.Category.objects.get(id=kwargs.get('pk'))
#         serializer = serializers.CategoryUpdateSerializer(data=request.data, instance=category)
#         if serializer.is_valid():
#             serializer.save(editor=self.request.user)
#         return Response(serializer.data)
#
#
# class CategoryDeleteView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def delete(self, request, *args, **kwargs):
#         category = models.Category.objects.get(id=kwargs.get('pk'))
#         category.delete()
#         return Response({'state': "deleted"})
