from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentListView.as_view()),
    path('create/', views.CommentCreateView.as_view()),
    path('<int:pk>/detail/', views.CommentDetailView.as_view()),
    path('<int:pk>/update/', views.CommentUpdateView.as_view()),
    path('<int:pk>/delete/', views.CommentDeleteView.as_view()),
]