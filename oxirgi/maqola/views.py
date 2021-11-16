from rest_framework import permissions, pagination, filters, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import serializers, models
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView,
    CreateAPIView
)
from .pagenation import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


class UserListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]


class ArticleListView(ListAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    pagination_class = CustomPagination


class ArticleCreateView(ListCreateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleCreateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(RetrieveAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticleUpdateView(RetrieveUpdateAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_update(self, serializer):
        serializer.save(editor=self.request.user)


class ArticleDeleteView(RetrieveDestroyAPIView):
    queryset = models.Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, ]


# class ArticleViewSets(ModelViewSet):
#     queryset = models.Article.objects.all()
#     serializer_class = serializers.ArticleSerializer
#
#
# class ArticleListView(APIView):
#     def get(self, request, *args, **kwargs):
#         article = models.Article.objects.all()
#         serializer = serializers.ArticleSerializer(article, many=True)
#         return Response(serializer.data)
#
#
# class ArticleCreateView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def post(self, request):
#         serializer = serializers.ArticleSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class ArticleDetailView(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             if kwargs.get('pk'):
#                 article = models.Article.objects.get(id=kwargs.get('pk'))
#                 serializer = serializers.ArticleSerializer(article, many=False)
#                 return Response(serializer.data)
#         except Exception:
#             raise NotFound("Category not found!")
#
#
# class ArticleUpdateView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def put(self, request, *args, **kwargs):
#         model = models.Article.objects.get(id=kwargs.get('pk'))
#         serializer = serializers.ArticleSerializer(data=request.data, instance=model)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class ArticleDeleteView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def delete(self, request, *args, **kwargs):
#         model = models.Article.objects.get(id=kwargs.get('pk'))
#         model.delete()
#         return Response({"deleted": "state"})
