from django.urls import path
from . import views

urlpatterns = [
    path('api/authors/', views.AuthorListCreate.as_view()),
    path('api/posts/', views.PostListCreate.as_view()),
]
