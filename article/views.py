from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Count, Avg, Max, Min

from article.forms import TopicForm
from article.models import Topic, User
import datetime
from django.views.generic.list import ListView


def get_topic_list(request):
    print(request.GET)
    print(request.GET.get('type'))
    context = {'topic_list': Topic.objects.all()}
    # context = {'topic_list': ['Topic 1', 'Topic 2', 'Topic 3']}
    return render(request, 'courses.html', context)


# Create - 2 variants
# Update - 2 variants
# Delete - ? variants

def create_topic(request):

    # Var.1
    # topic = Topic(title='Django ORM', text='Wea re learning Django', type=4)
    # topic.subtitle = 'My subtitle'
    # topic.save()

    # Var.2
    topic = Topic.objects.create(title='Django ORM', text='Wea re learning Django', type=4)
    return render(request, 'courses.html', {'topic_list': [topic]})


def update_topic(request):

    # Var.1
    topic = Topic.objects.get(id=4)
    # topic.author = User.objects.get(username='Serhii')
    # topic.save()
    data = {'text': 'New text', 'subtitle': 'My subtitle',
            'url': 'https://w3schoolsua.github.io/django/index.html'}
    # for key, value in data.items():
    #     setattr(topic, key, value)
    # topic.save()
    # return render(request, 'courses.html', {'topic_list': [topic]})
    # Var.2
    topic = Topic.objects.filter(id=4)
    topic.update(**data)
    return render(request, 'courses.html', {'topic_list': topic})


def delete_topic(request):
    # Var.1
    topic = Topic.objects.get(id=4)
    topic.delete()
    # Var.2
    Topic.objects.filter(id=4).delete()
    return render(request, 'courses.html', {'topic_list': Topic.objects.all()})


"""FILTER"""
def filter_topic(request):
    # Get all records in table
    all_records = Topic.objects.all()

    # Get records with conditions
    # topics = Topic.objects.filter(type=5)
    # topics = Topic.objects.filter(type__range=(1, 5))
    # topics = Topic.objects.filter(type=5, title__contains='python')
    # topics = Topic.objects.filter(author__username__contains='Codia')
    # topics = Topic.objects.filter(author__username__contains='Serhii').count()
    # topics = Topic.objects.filter(author__username__contains='Serhii').first()
    # topics = Topic.objects.filter(author__username__contains='Serhii').last()
    # topics = Topic.objects.filter(author__username__contains='Codia').exists()
    # topics = Topic.objects.filter(author__username__contains='Serhii').order_by('creation_date').distinct('type')
    # # Вибрати першу статтю відповідного типу
    # topics = Topic.objects.exclude(url__isnull=True)
    # topics = Topic.objects.filter(type=5).exclude(author_id=3)
    # now_ = datetime.datetime.now()
    # topics = Topic.objects.filter(type=4).union(
    #     Topic.objects.filter(creation_date__range=(now_ - datetime.timedelta(days=2))))
    # topics = Topic.objects.annotate('type')  # Групування за типом
    topics = Topic.objects.annotate(Count('author'))
    return render(request, 'courses.html', {'topic_list': topics})


def create_topic_form(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            # topic = Topic.objects.create(**form.cleaned_data)
            # return render(request, 'courses.html', {'topic_list': topic})
            Topic.objects.create(**form.cleaned_data)
            return redirect('topic_list')
    else:
        form = TopicForm()
        return render(request, 'contact.html', {'form': form})


class TopicListView(ListView):
    queryset = Topic.objects.all()  # або model = Topic
    template_name = 'courses.html'

    









