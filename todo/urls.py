from django.conf.urls import patterns, include, url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),

)
