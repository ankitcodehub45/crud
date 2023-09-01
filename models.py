from operator import mod
from statistics import mode
from tkinter.tix import MAX
from django.db import models

class crudajax(models.Model):
    fname = models.CharField(max_length=50,null=False)
    lname = models.CharField(max_length=50)
    mymail = models.EmailField(max_length=100,null=False)
    mypswd = models.CharField(max_length=50,null=False)
    createdon = models.DateTimeField(auto_now=True,null=False)
    delete_flag = models.BooleanField(default=False)
