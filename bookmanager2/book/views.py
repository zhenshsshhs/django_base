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


############## delete data in the database #####################
"""
    There are two forms of deletion:
        1.logical deletion (set the flag of the item of is_delete in database.
        2.physical deletion (delete the items  in the database directly. 
    
    below functions are physical deletion.
"""
# the one of physical deletion way
book = BookInfo.objects.get(id=6)
book.delete()

# the second of physical deletion way
BookInfo.objects.get(id = 6).delete()
BookInfo.objects.filter(id = 5).delete()
