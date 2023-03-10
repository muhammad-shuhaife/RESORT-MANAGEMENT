from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Backend.models import admindb,customerdb,roomdb,roomtypedb
from Frontend.models import savecontactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
# Create your views here.

def viewlogin(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method == "POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')

        if User.objects.filter(username__contains = username_r).exists():
            user = authenticate(username = username_r, password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                messages.success(req, "Login Successfully")
                return redirect(indexpage)
            else:
                messages.error(req, "Invalid User")
        return redirect(viewlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(viewlogin)


def indexpage(request):
    data = savecontactdb.objects.all()
    return render(request,"index.html",{'data':data})
def addadmin(request):
    return render(request,"add_admin.html")
def saveadmin(req):
    if req.method== "POST":
        USERNAME = req.POST.get('name')
        EMAIL=req.POST.get('email')
        PASSWORD = req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('confirmpassword')
        IMAGE = req.FILES['image']
        obj=admindb(Name=USERNAME,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Email=EMAIL,Image=IMAGE)
        obj.save()
        return redirect(addadmin)
def viewadmin(request):
    data = admindb.objects.all()
    return render(request,"view_admin.html",{'data':data})
def editadmin(request,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(request,"edit_admin.html",{'data':data})
def updateadmin(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        EMAIL = req.POST.get('email')
        PASSWORD = req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('confirmpassword')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).Image
        admindb.objects.filter(id=dataid).update(Name=NAME,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Email=EMAIL,Image=file)
        return redirect(viewadmin)
def deleteadmin(request,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewadmin)




def addcustomer(request):
    return render(request,"add_customer.html")
def savecustomer(req):
    if req.method== "POST":
        NAME = req.POST.get('name')
        EMAIL=req.POST.get('email')
        AGE = req.POST.get('age')
        ADDRESS = req.POST.get('address')
        DATEIN = req.POST.get('datein')
        DATEOUT = req.POST.get('dateout')
        MOBILE = req.POST.get('mobile')
        IMAGE = req.FILES['image']
        obj=customerdb(Name=NAME,Age=AGE,Address=ADDRESS,Email=EMAIL,Datein=DATEIN,Dateout=DATEOUT,Mobile=MOBILE,Document=IMAGE)
        obj.save()
        return redirect(addcustomer)
def viewcustomer(request):
    data = customerdb.objects.all()
    return render(request,"view_customer.html",{'data':data})
def editcustomer(request,dataid):
    data=customerdb.objects.get(id=dataid)
    print(data)
    return render(request,"edit_customer.html",{'data':data})
def updatecustomer(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        EMAIL = req.POST.get('email')
        AGE = req.POST.get('age')
        ADDRESS = req.POST.get('address')
        DATEIN = req.POST.get('datein')
        DATEOUT = req.POST.get('dateout')
        MOBILE = req.POST.get('mobile')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = customerdb.objects.get(id=dataid).Document
        customerdb.objects.filter(id=dataid).update(Name=NAME,Age=AGE,Address=ADDRESS,Email=EMAIL,Datein=DATEIN,Dateout=DATEOUT,Mobile=MOBILE,Document=file)
        return redirect(viewcustomer)
def deletecustomer(request,dataid):
    data=customerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcustomer)


def addroomt(request):
    return render(request,"add_roomt.html")
def saveroomt(req):
    if req.method== "POST":
        DESCRIPTION = req.POST.get('decription')
        TYPE=req.POST.get('type')
        IMAGE = req.FILES['image']
        obj=roomtypedb(Description=DESCRIPTION,Type=TYPE,Image=IMAGE)
        obj.save()
        return redirect(addroomt)
def viewroomt(request):
    data = roomtypedb.objects.all()
    return render(request,"view_roomt.html",{'data':data})
def editroomt(request,dataid):
    data=roomtypedb.objects.get(id=dataid)
    print(data)
    return render(request,"edit_roomt.html",{'data':data})
def updateroomt(req,dataid):
    if req.method=="POST":
        DESCRIPTION = req.POST.get('description')
        TYPE = req.POST.get('type')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = roomtypedb.objects.get(id=dataid).Image
        roomtypedb.objects.filter(id=dataid).update(Description=DESCRIPTION,Type=TYPE,Image=file)
        return redirect(viewroomt)
def deleteroomt(request,dataid):
    data=roomtypedb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewroomt)


def addroom(request):
    data = roomtypedb.objects.all()
    return render(request,"add_room.html",{'data':data})
def saveroom(req):
    if req.method== "POST":
        NAME = req.POST.get('name')
        TYPE=req.POST.get('type')
        COUNT = req.POST.get('count')
        PRICE = req.POST.get('price')
        IMAGE = req.FILES['image']
        IMAGE2 = req.FILES['image2']
        IMAGE3 = req.FILES['image3']
        obj=roomdb(Name=NAME,Type=TYPE,Count=COUNT,Price=PRICE,Image=IMAGE,Image2=IMAGE2,Image3=IMAGE3)
        obj.save()
        return redirect(addroom)
def viewroom(request):
    data = roomdb.objects.all()
    return render(request,"view_room.html",{'data':data})
def editroom(request,dataid):
    data=roomdb.objects.get(id=dataid)
    da = roomtypedb.objects.all()
    print(data)
    return render(request,"edit_room.html",{'data':data, 'da':da})
def updateroom(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        TYPE = req.POST.get('type')
        COUNT = req.POST.get('count')
        PRICE = req.POST.get('price')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = roomdb.objects.get(id=dataid).Image

        roomdb.objects.filter(id=dataid).update(Name=NAME,Type=TYPE,Count=COUNT,Price=PRICE,Image=file)
        return redirect(viewroom)
def deleteroom(request,dataid):
    data=roomdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewroom)
def viewmessage(request):
    data = savecontactdb.objects.all()
    return render(request,"view_messages.html",{'data':data})
def deletemessage(request,dataid):
    data=savecontactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewmessage)

