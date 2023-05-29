from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('top/', views.top, name="top" ),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]