from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Backend.models import customerdb,roomdb,roomtypedb
from Frontend.models import registrationdb,savecontactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
import random


# Create your views here.
def loginfront(request):
    return render(request,"loginf.html")
def loginfrontf(request):
    if request.method=='POST':
        username_r=request.POST.get("usernamel")
        password_r = request.POST.get("passwordl")
        if registrationdb.objects.filter(Name=username_r,Password=password_r).exists():
            request.session['usernamel']=username_r
            request.session['passwordl'] = password_r
            messages.success(request,"Login Successfully")
            return redirect(fronthomepage)
        else:
            messages.error(request, "Invalid User")
            return render(request,'loginf.html',{'msg':"sorry...invalid username or password"})
def logoutfront(request):
    del request.session['usernamel']
    del request.session['passwordl']
    messages.success(request, "Logged Out Successfully")
    return redirect(loginfront)
def saveregistration(req):
    if req.method== "POST":
        NAME=req.POST.get('username')
        EMAIL=req.POST.get('email')
        PASSWORD=req.POST.get('password')
        CONFIRMPASSWORD = req.POST.get('confirmpassword')
        obj=registrationdb(Name=NAME,Email=EMAIL,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD)
        obj.save()
        messages.success(req,"Registered Successfully")
        return redirect(loginfront)

def savecontact(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        SUBJECT=req.POST.get('subject')
        MESSAGE=req.POST.get('message')
        obj=savecontactdb(Name=NAME,Email=EMAIL,Subject=SUBJECT,Message=MESSAGE)
        obj.save()
        messages.success(req,"Sent Successfully")
        return redirect(contact)



def fronthomepage(request):
    data = roomtypedb.objects.all()
    return render(request, "homepage.html", {'data': data})
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")
def roomsf(request,):
    data = roomtypedb.objects.all()
    return render(request, "rooms_f.html", {'data': data})

def displayroompage(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = roomdb.objects.filter(Type=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(request,"viewroomf.html",context)
def viewsingleroompage(req,dataid):
    data=roomdb.objects.filter(id=dataid)
    return render(req,"room_single.html",{'dat':data})



def invoicef(request):
    invoice_number = random.randint(10000, 99999)
    # Retrieve the form data from the POST request
    name = request.POST.get('name')
    mobile = request.POST.get('mobile')
    address = request.POST.get('address')
    checkindate = request.POST.get('checkindate')
    checkoutdate = request.POST.get('checkoutdate')
    type = request.POST.get('type')
    count = request.POST.get('count')
    image = request.POST.get('image')

    # Render the invoice template with the form data as context
    context = {
        'name': name,
        'mobile': mobile,
        'address': address,
        'checkindate': checkindate,
        'checkoutdate': checkoutdate,
        'type': type,
        'count': count,
        'image': image,
        'invoice_number': invoice_number
    }
    return render(request, 'invoice.html', context=context)

def savecustomerf(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        MOBILE=req.POST.get('mobile')
        ADDRESS=req.POST.get('address')
        CIN=req.POST.get('checkindate')
        COUT = req.POST.get('checkoutdate')
        TYPE = req.POST.get('type')
        COUNT = req.POST.get('count')
        INVOICE = req.POST.get('invoice_number')

        obj=customerdb(Name=NAME,Mobile=MOBILE,Address=ADDRESS,Datein=CIN,Dateout=COUT,Room=TYPE,Invoice=INVOICE)
        obj.save()
        messages.success(req,"Booked Successfully")
        return redirect(roomsf)




