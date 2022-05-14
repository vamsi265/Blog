from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('update/<int:pk>/', views.PostUpdate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]