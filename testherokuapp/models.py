from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.


class Candidate(models.Model):
    file_created = models.DateTimeField(default=timezone.now)
    firstname = models.CharField(max_length=50,null=True)
    lastname = models.CharField(max_length=50,null=True)
    contactdetails = models.IntegerField(null=True)
    emailid = models.EmailField(unique=True, null=True)
    addressdetails = models.CharField(max_length=500, null=True)
    workexperience = models.CharField(max_length=20, null=True)
    visastatus = models.CharField(max_length=20, null=True)
    workpermit = models.CharField(max_length=100, null=True)
    readytorelocate = models.CharField(max_length=20, null=True)
    technology = models.TextField(max_length=200, null=True)


class Meta:
    db_table = "Candidate"
