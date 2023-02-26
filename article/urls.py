from django.contrib import admin
from django.urls import path
from article.views import *

urlpatterns = [
    # path('topics/', get_topic_list, name='topic_list'),  # http://127.0.0.1:8000/articles/topics/
    path('topics/', TopicListView.as_view(), name='topic_list'),
    path('topics_list/', get_topic_list, name='function_topic_list'),
    path('create/', create_topic),  # http://127.0.0.1:8000/articles/create/
    path('update/', update_topic),  # http://127.0.0.1:8000/articles/update/
    path('delete/', delete_topic),  # http://127.0.0.1:8000/articles/delete/
    # path('create/form/', create_topic_form),  # http://127.0.0.1:8000/articles/create/form/
    path('create/form', TopicFormView.as_view()),
    # path('create/form1/', create_topic_form1),  # http://127.0.0.1:8000/articles/create/form1/
    path('topics/<int:pk>', get_single_topic)
]
