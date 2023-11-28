from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    host = request.META['HTTP_HOST'],
    user_agent = request.META['HTTP_USER_AGENT'],
    ip = request.META['REMOTE_ADDR'],

    text = f'host: {host}, bro: {user_agent}, ip:{ip}'
    return HttpResponse(text, headers={'SecretCod': '12313'})


def user(request, login = 'Nologin', Nameofpapka = 'Noname', num = 0):
    return HttpResponse (f'login: {login}. Nameofpapka: {Nameofpapka}, num: {num}')


def error(request):
    return HttpResponseNotFound('К сожалению произошла ошибка', status=400, reason='Incorrect data')