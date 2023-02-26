from django.test import TestCase
from django.test import Client
from django.urls import reverse
from article.views import *


# Create your tests here.
class TopicTest(TestCase):
    # Запускаємо: python manage.py test article.tests

    def setUp(self):
        self.test_topic = Topic.objects.create(
            title='Test Topic', text='My test text',
            url='http://127.0.0.1:8000/', type=1)

    def test_topic_creation(self):
        topic = Topic.objects.create(
            title='Test topic', text='My test text',
            url='http://127.0.0.1:8000/', type=1)  # Створюємо об'єкт topic
        self.assertTrue(isinstance(topic, Topic))  # перевіряємо чи topic є об'єктом класу Topic
        database_topic = Topic.objects.get(title='Test topic')  # Отримуємо з бази даних об'єкт database_topic
        self.assertEqual(topic, database_topic)  # Перевіряємо чи є topic еквівалентним database_topic

    def test_get_topic(self):
        database_topic = Topic.objects.get(title='Test Topic')
        self.assertEqual(database_topic, self.test_topic)

    def test_topic_update(self):
        topic = Topic.objects.filter(title='Test Topic')
        self.assertEqual(self.test_topic, topic.first())  # Порівняємо self.test_topic з
        # першим елементом queryset-у topic
        topic.update(text='Updated text')
        new_topic = Topic.objects.get(title='Test Topic')
        self.assertEqual(new_topic.text, 'Updated text')

    def test_topic_delete(self):
        self.test_topic.delete()
        self.assertFalse(Topic.objects.filter(title='Test Topic').exists())


class ArticleViewTest(TestCase):

    def test_getting_topic_list(self):
        url = reverse('topic_list')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers.get('Content-Type'))

    def test_getting_function_topic_list(self):
        url = reverse('function_topic_list')
        response = self.client.get(url)
        print(response)
        print(response.headers)
        self.assertIn('text/html', response.headers.get('Content-Type'))


class TopicFormTest(TestCase):

    def setUp(self) -> None:
        self.topic = Topic.objects.create(
            title='Test topic', text='My test text',
            url='http://127.0.0.1:8000/', type=1)

    def test_creation_topic_form__valid(self):

        data = {'title': self.topic.title, 'subtitle': '1', 'text': self.topic.text, 'url': self.topic.url, 'type': 1}
        form = TopicForm(data=data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_creation_topic_form__invalid(self):
        data = {'title': self.topic.title, 'text': self.topic.text, 'url': self.topic.url, 'type': 1}
        form = TopicForm(data=data)
        print(form.errors)
        self.assertFalse(form.is_valid())


class TopicClientTest(TestCase):
    def setUp(self) -> None:
        self.test_topic = Topic.objects.create(title='Django ORM', text='We are learning Django', type=4)
        self.client = Client()

    def test_article_create_client(self):
        # response = self.client.get('article/topic/create/')
        # self.assertEqual(response.status_code, 200)
        self.assertTrue(Topic.objects.filter(title='Django ORM').exists())

    def test_article_update_client(self):
        url ='article/topic/update/'
        response = self.client.get(url)
        print(response)
        print(response.headers)

        topic = Topic.objects.get(title='Django ORM')
        self.assertEqual(topic.text, 'We are learning Django')
        # self.assertEqual(response.status_code, 200)




