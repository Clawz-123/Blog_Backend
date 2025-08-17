from django.urls import path
from . import views


urlpatterns = [
    path('user-blogs/', views.UserBlogView.as_view(), name='user_blogs'),
    path('create-blog/', views.BlogCreateView.as_view(), name='create_blog'),
    path('update-blog/<uuid:pk>/', views.BlogUpdateView.as_view(), name='update_blog'),
    path('delete-blog/<uuid:pk>/', views.BlogDeleteView.as_view(), name='delete_blog'),
]
