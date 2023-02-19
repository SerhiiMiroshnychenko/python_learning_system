from django.contrib import admin
from django.urls import path
from article.views import *

urlpatterns = [
    path('topics/', get_topic_list, name='topic_list'),  # http://127.0.0.1:8000/articles/topics/
    path('create/', create_topic),  # http://127.0.0.1:8000/articles/create/
    path('update/', update_topic),  # http://127.0.0.
    path('delete/', delete_topic),  # http://127.0.0
    path('create/form/', create_topic_form),  # http://127.0.0.1:8000/articles/create/form/
]

