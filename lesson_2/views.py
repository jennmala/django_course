from django.shortcuts import render
from django.http import HttpResponse
# from http import HTTPStatus


def index(request):
    return render(request, 'index.html')


def bio(request, username):
    print(username)
    return render(request, 'index.html')


def year_archive(request, year):
    print(request)
    print(year)
    print(HttpResponse(f'{year}'))

    return HttpResponse(f'{year}')


def something_not_found(request):
    response = HttpResponse('Not found what you want')
    response.status = 404
    return response
