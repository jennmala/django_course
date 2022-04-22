from datetime import date
from http.client import HTTPResponse
from telnetlib import GA
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
import csv

from lesson_8.models import GameModel

def upload_data(request):
    with open('vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:

            try:
                obj, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
                print(row)
            except:
                pass

    return HttpResponse('Done!')         



class FilterViews(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name='Hitman (2016)')
    # queryset = GameModel.objects.filter(name__contains='Hitman')



class ExcludeViews(ListView):
    template_name = 'gamemodel_list.html' 
    queryset = GameModel.objects.exclude(name__contains='Hitman')



class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    # queryset = GameModel.objects.exclude(name__contains='Hitman').order_by('year')
    queryset = GameModel.objects.exclude(name__contains='Hitman').order_by('-year')
    # queryset = GameModel.objects.exclude(name__contains='Hitman').order_by('year').reverse()



class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


class UnionView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name='Hitman (2016)').union( GameModel.objects.filter(name='Tetris'))


class NoneView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.none()


class ValuesView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name='Hitman (2016)').values('name', 'platform')

    # def get(self, request, *args, **kwargs):
    #     print(list(
    #         GameModel.objects.filter(name='Hitman (2016)').values_list('name', 'platform' , flat=True)
    
    #     ))
        
    #     return super().get(request, *args, **kwargs)


def date_view(request):
    data = GameModel.objects.dates(field_name='year', kind='month')
    print(data)
    return HttpResponse(data)


def get_view(request):
    data = GameModel.objects.get(id=1)
    # data = GameModel.objects.get(name='Hitman (2016)')
    print(data)
    return HttpResponse(data)
   
