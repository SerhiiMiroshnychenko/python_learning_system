from django.contrib import admin
from django.urls import path
from article.views import get_topic_list

urlpatterns = [
    path('topics/', get_topic_list),  # http://127.0.0.1:8000/articles/topics/
]

