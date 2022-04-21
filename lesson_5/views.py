from decimal import Decimal
from django.http import HttpResponse
from lesson_5.models import Flower, Bouquet, Client
from uuid import uuid4
from django.core.files import File
from django.contrib.auth.models import User



def create_flower(request):
    rose = Flower()
    rose.count = 5
    rose.description = 'about rose'
    rose.could_use_in_bouquet = True
    rose.wiki_page = 'https://www.wikipedia.org/wiki/Rose'
    rose.name = 'Rose'
    rose.save()
    return HttpResponse('Created!')


def create_client(request):    
    client = Client.objects.create(**{
        'user': User.objects.get(pk=1),
        'second_email': 'admin@admin1.com',
        'name': 'MyName5',
        'invoice': File(open('requirements.txt')),
        'user_uuid': uuid4(),
        'discount_size': Decimal('0.00052'),
        'client_ip': '192.0.2.1',
    })
    print(client)
    return HttpResponse(client)


def get_flower(request):
    price = Bouquet.shop.get(id=1).price
    return HttpResponse(price)



