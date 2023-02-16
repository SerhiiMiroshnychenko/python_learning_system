from django.shortcuts import render
from django.http import HttpResponse
from article.models import Topic


def get_topic_list(request):
    context = {'topic_list': Topic.objects.all()}
    # context = {'topic_list': ['Topic 1', 'Topic 2', 'Topic 3']}
    return render(request, 'courses.html', context)


