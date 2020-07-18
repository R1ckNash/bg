from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    #path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^beers/$', views.BeerListView.as_view(), name='beers'),
    url(r'^beer/(?P<pk>\d+)$', views.BeerDetailView.as_view(), name='beer-detail'),
    url(r'^producers/$', views.ProducerListView.as_view(), name='producers'),
    url(r'^producer/(?P<pk>\d+)$', views.ProducerDetailView.as_view(), name='producer-detail'),
]
