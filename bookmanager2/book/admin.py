from django.contrib import admin

# Register your models here.
from book.models import PeopleInfo,BookInfo

admin.site.register(PeopleInfo)
admin.site.register(BookInfo)