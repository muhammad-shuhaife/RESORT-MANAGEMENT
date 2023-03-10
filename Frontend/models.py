from django.db import models

# Create your models here.
class registrationdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Password=models.CharField(max_length=30,null=True,blank=True)
    Confirmpassword=models.CharField(max_length=30,null=True,blank=True)

class savecontactdb(models.Model):
    Name=models.CharField(max_length=30,null=True,blank=True)
    Email=models.EmailField(max_length=30,null=True,blank=True)
    Subject=models.CharField(max_length=30,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)