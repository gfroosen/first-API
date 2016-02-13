from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    'api.views',
    url(r'^tasks/$', 'task_list', name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
    url(r'^list$', views.list, name='list'),
    url(r'^$', views.index, name='index'),


)
