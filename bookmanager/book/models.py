from django.db import models

# Create your models here.

"""
1. the data table need to create a class inherited by models.Model
2. the primary key of id is created automatically
3. Don't use the keyword in Python and SQL as the field name
    field_name = models.TYPE(max_length=10)
"""


class BookInfo(models.Model):
    # the primary key of id is created automatically
    name = models.CharField(max_length=50)

class PeopleInfo(models.Model):
    name = models.CharField(max_length=50)
    gender =models.BooleanField()
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)