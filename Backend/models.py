from django.db import models

# Create your models here.
class admindb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=30,null=True,blank=True)
    Image=models.ImageField(upload_to="admin",blank=True,null=True)


class customerdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Datein=models.CharField(max_length=30,null=True,blank=True)
    Dateout=models.CharField(max_length=30,null=True,blank=True)
    Mobile=models.IntegerField(blank=True,null=True)
    Room=models.CharField(max_length=30, null=True, blank=True)
    Invoice = models.CharField(max_length=30, null=True, blank=True)
    Address = models.CharField(max_length=30, null=True, blank=True)
    Document=models.ImageField(upload_to="customer",blank=True,null=True)

class roomtypedb(models.Model):
    Description = models.CharField(max_length=30, null=True, blank=True)
    Image=models.ImageField(upload_to="room",blank=True, null=True)
    Type=models.CharField(max_length=30,null=True,blank=True)

class roomdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Type=models.CharField(max_length=30,null=True,blank=True)
    Count=models.IntegerField(null=True,blank=True)
    Price=models.CharField(max_length=30,null=True,blank=True)
    Image = models.ImageField(upload_to="roomsingle", blank=True, null=True)
    Image2 = models.ImageField(upload_to="roomsingle", blank=True, null=True)
    Image3 = models.ImageField(upload_to="roomsingle", blank=True, null=True)
