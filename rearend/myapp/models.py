from django.db import models

# Create your models here.


class Router(models.Model):
    rname = models.CharField(max_length=20)
    rdate = models.DateTimeField()
    rposition = models.IntegerField()
    rnumberport = models.IntegerField()
    IsDelete = models.BooleanField(default=False)


class Port(models.Model):
    pname = models.CharField(max_length=20)
    paddress = models.CharField(max_length=40)
    pstatus = models.BooleanField(default=False)
    pvlan = models.CharField(max_length=20)
    IsDelete = models.BooleanField(default=False)
    prouter = models.ForeignKey('Router', on_delete=models.CASCADE)