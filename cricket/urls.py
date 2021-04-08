#assert isinstance(path, object)
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('home',views.home, name='home'),
    url('scoreboard/(?P<id>\w+)',views.scoreboard, name='scoreboard')
]