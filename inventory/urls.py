from django.conf.urls import url
from . import views

app_name = 'inventory'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<reagent_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<reagent_id>[0-9]+)/change/$', views.change, name='change'),
]
