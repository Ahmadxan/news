from django.urls import path
from accounts.views import CustomUserListView, CustomUserCreateView, AdminCreateListView, GroupCreateView, \
    UsersRetrieveDestroyAPIView

urlpatterns = [
    path('', CustomUserListView.as_view()),
    path('create/', CustomUserCreateView.as_view()),
    path('delete/', UsersRetrieveDestroyAPIView.as_view()),

    path('admin/create/', AdminCreateListView.as_view()),

    path('group/create/', GroupCreateView.as_view()),
]