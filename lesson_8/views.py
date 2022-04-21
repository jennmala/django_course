from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
import csv

from lesson_8.models import GameModel

def upload_data(request):
    with open('./vgsales.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            try:
                _, created = GameModel.objects.get_or_create(
                    name=row[1],
                    platform=row[2],
                    year=datetime.date(int(row[3]), 1, 1),
                    genre=row[4],
                    publisher=row[5],
                    na_sales=row[6],
                    eu_sales=row[7],
                    jp_sales=row[8],
                    other_sales=row[9],
                    global_sales=row[10],
                )
            except:
                pass
    return HttpResponse('Done!')         



class FilterViews(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.filter(name='Hitman (2016)')



class ExcludeViews(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains='Hitman')



class OrderByView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.exclude(name__contains='Hitman').order_by('year')



class AllView(ListView):
    template_name = 'gamemodel_list.html'
    queryset = GameModel.objects.all()


# class UnionView(ListView):
#     template_name = 'gamemodel_list.html'
#     queryset = GameModel.objects.exclude(name__contains='Hitman').order_by('year')



    
