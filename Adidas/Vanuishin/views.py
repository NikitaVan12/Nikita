from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META['HTTP_HOST'],
    user_agent = request.META['HTTP_USER_AGENT'],
    path = request.path,
    ip = request.META['REMOTE_ADDR'],

    text = f'host: {host}, bro: {user_agent}, ip:{ip}'
    return HttpResponse(text, headers={'SecretCod': '12313'})


def user(request, name = 'Noname', age = 0):
    return HttpResponse (f'User: {name}. Age: {age}')