from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # Функція, що імплементує цей конкретний view
    # Щоби ця функція спрацювала, вона повинна бути прив'язана дор якогось запиту URL
    return HttpResponse("Hello, world. Greetings from Beetroot Academy!")
    # HttpResponse -> функція, що повертає в браузер текстову відповідь,
    # передану їй як аргумент

