from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=50,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookinfo'

class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (0,'male'),
        (1,'female')
    )
    name = models.CharField(max_length=50,unique=True)
    gender = models.BooleanField(choices=GENDER_CHOICE,default=0)
    description = models.CharField(max_length=50)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'peopleinfo'