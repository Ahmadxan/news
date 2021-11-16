from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('create/', views.ArticleCreateView.as_view()),
    path('<int:pk>/detail/', views.ArticleDetailView.as_view()),
    path('<int:pk>/update/', views.ArticleUpdateView.as_view()),
    path('<int:pk>/delete/', views.ArticleDeleteView.as_view()),
]