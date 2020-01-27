from django.urls import path
from .views import article_list_view, article_detail

urlpatterns = [
    path('article/', article_list_view),
    path('detail/<int:pk>/', article_detail),
]