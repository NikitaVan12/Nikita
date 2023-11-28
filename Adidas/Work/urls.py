from django.urls import path, include, re_path

from . import views
from .views import *

urlpatterns = [
    re_path(r'^user/(?P<login>\D+)/(?P<Nameofpapka>\D+)/(?P<num>\d+)/', views.user),
    path('', index, name='home'),
    path('error/', error),


]



#  path('user/<str:login>/<str:Nameofpapka>/<int:num>/', user, name='user')