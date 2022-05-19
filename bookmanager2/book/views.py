from django.http import HttpResponse,HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("ok")



############## add database #####################

# the one of way
from book.models import BookInfo
book=BookInfo(
    name ='django',
    pub_date='2020-01-01',
    readcount=10
)
book.save()

# the second of way
from book.models import BookInfo
BookInfo.objects.create(
    name ='development test',
    pub_date='2020-01-02',
    readcount=100
)

############## update data in the database #####################

book = BookInfo.objects.get(id=6)
book.name = 'operation development'
book.save()


BookInfo.objects.filter(id=6).update(name='crawler')