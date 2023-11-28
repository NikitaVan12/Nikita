from django.urls import path, include, re_path
from .views import index, user


urlpatterns = [
    path('', index, name = 'home'),
    re_path(r'^user/(?P<name>\d+)/(?P<age>\d+)', user),
    re_path(r'^user', user)
    # path('user', user, name = 'user')
]