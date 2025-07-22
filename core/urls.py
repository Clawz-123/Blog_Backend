from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API for blog posts and categories.",
        terms_of_service="https://yourdomain.com/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('api/', include(('blog_api.urls', 'blog_api'), namespace='blog_api')),

    # Swagger Docs
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
