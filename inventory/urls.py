from django.conf.urls import url, include
from django.views.generic import ListView
from . import views
from inventory.models import reagent

app_name = 'inventory'
urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^index$', ListView.as_view(queryset=reagent.objects.all(), template_name="inventory/index.html"), name ="index"),
    url(r'^(?P<reagent_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<reagent_id>[0-9]+)/change/$', views.change, name='change'),
]


# app_name = 'inventory'
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<reagent_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<reagent_id>[0-9]+)/change/$', views.change, name='change'),
# ]
