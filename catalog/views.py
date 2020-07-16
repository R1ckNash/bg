from django.shortcuts import render

from .models import Beer, Producer, Style, Category


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_beers = Beer.objects.all().count()
    num_producers = Producer.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_beers': num_beers, 'num_producers': num_producers},
    )
