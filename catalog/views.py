from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from .models import Beer, Producer, Style, Category
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
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

@csrf_protect
def registration(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request,newuser)
            return HttpResponseRedirect('/')
        else:
            args['form'] = newuser_form
    return render(request,'registration/registration.html',args)


class BeerListView(LoginRequiredMixin, generic.ListView):
    model = Beer
    paginate_by = 10


class BeerDetailView(generic.DetailView):
    model = Beer


class ProducerListView(LoginRequiredMixin, generic.ListView):
        model = Producer
        paginate_by = 10


class ProducerDetailView(generic.DetailView):
        model = Producer