from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
               path('', TemplateView, {'template': 'karate.html'}, name='karate-home'),
               re_path(r'^swingtime/events/type/([^/]+)/$', views.event_type, name='karate-event'),
               path('swingtime/', include('swingtime.urls')),
               ]
