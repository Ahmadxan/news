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
from maqola.pagenation import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend


class UserListView(ListAPIView):
    filter_backends = [DjangoFilterBackend]


class CommentListView(ListAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    pagination_class = CustomPagination


class CommentCreateView(ListCreateAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentCreateSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(RetrieveAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


# class CommentUpdateView(RetrieveUpdateAPIView):
#     queryset = models.Comment.objects.all()
#     serializer_class = serializers.CommentUpdateSerializer
#     permission_classes = [permissions.IsAuthenticated, ]
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


# class CommentDeleteView(RetrieveDestroyAPIView):
#     queryset = models.Comment.objects.all()
#     serializer_class = serializers.CommentSerializer
#     permission_classes = [permissions.IsAuthenticated, ]


class CommentViewSets(ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

#
#
# class CommentListView(APIView):
#     def get(self, request, *args, **kwargs):
#         comment = models.Comment.objects.all()
#         serializer = serializers.CommentSerializer(comment, many=True)
#         return Response(serializer.data)
#
#
# class CommentCreateView(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def post(self, request):
#         serializer = serializers.CommentSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class CommentDetailView(APIView):
#     def get(self, request, *args, **kwargs):
#         try:
#             if kwargs.get('pk'):
#                 comment = models.Comment.objects.get(id=kwargs.get('pk'))
#                 serializer = serializers.CommentSerializer(comment, many=False)
#                 return Response(serializer.data)
#         except Exception:
#             raise NotFound("Comment not found!")


class CommentUpdateView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        model = models.Comment.objects.get(id=kwargs.get('pk'))
        if model.user == self.request.user:
            serializer = serializers.CommentUpdateSerializer(data=request.data, instance=model)
            if serializer.is_valid():
                serializer.save(user=self.request.user)
            return Response(serializer.data)
        else:
            return Response({"state": "siz kommentni tahrirlay olmaysiz!"})


class CommentDeleteView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        model = models.Comment.objects.get(id=kwargs.get('pk'))
        if model.user == self.request.user:
            model.delete()
            return Response({"deleted": "state"})
        else: return Response("Siz Ochirish huquqiga ega emassiz")
