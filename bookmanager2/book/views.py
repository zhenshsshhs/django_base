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


"""基本查询"""
#
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常。
try:
    BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print('BookInfo matching query does not exist.')


# all查询多个结果。
BookInfo.objects.all()

# count查询结果数量。
BookInfo.objects.all().count()
BookInfo.objects.count()


"""过滤查询"""
#
# 实现SQL中的where功能，包括
#     filter过滤出多个结果   -->return list
#     exclude排除掉符合条件剩下的结果
#     get过滤单一结果

# 对于过滤条件的使用，上述三个方法相同，故仅以filter进行讲解。
# 属性名称__比较运算符=值
#
# # 属性名称和比较运算符间使用两个下划线，所以属性名不能包括多个下划线

# 查询编号为1的图书
BookInfo.objects.get(id__exact=1) # --> BookInfo.objects.filter(id__exact=1) [0]

BookInfo.objects.get(pk=1)  # pk  stand for primary key

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号大于3的图书
BookInfo.objects.filter(id__gt=3) #  gt --> greater than
                                  #  lt --> leaster than
# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1999-01-01')