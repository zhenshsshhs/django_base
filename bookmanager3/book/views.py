from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.

def create_book(request):
    BookInfo.objects.create(
        name = 'abc',
        pub_date='2020-1-1',
        readcount=100
    )
    return HttpResponse('create')

def shop(request,city_id,shop_id):

    query_params = request.GET
    wq = query_params.get('wq')
    order = query_params.getlist('order_by')
    print(wq)
    print(order)
    return HttpResponse(city_id,shop_id)