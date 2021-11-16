from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='News Api',
        description='News api uchun',
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email='xushvaqtovahmad98@gmail.com'),
        license=openapi.License(name="Proyekt litsenziyasi"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,)
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('articles/', include('maqola.urls')),
    path('categories/', include('category.urls')),
    path('comments/', include('comment.urls')),
    path('users/', include('accounts.urls')),

    # path('users/', include('user.urls')),

    path('auth-api/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('django.contrib.auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('accounts/', include('allauth.urls')),

    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0
    ), name='schema-swagger-ui'),
]
