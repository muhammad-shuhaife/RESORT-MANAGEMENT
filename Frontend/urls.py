from django.urls import path
from Frontend import views

urlpatterns = [
    path('loginfront/',views.loginfront,name="loginfront"),
    path('logoutfront/',views.logoutfront,name="logoutfront"),
    path('loginfrontf/', views.loginfrontf, name="loginfrontf"),
    path('saveregistration/', views.saveregistration, name="saveregistration"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('fronthomepage/',views.fronthomepage,name="fronthomepage"),
    path('about/',views.about,name="about"),
    path('contact/', views.contact, name="contact"),
    path('roomsf/', views.roomsf, name="roomsf"),
    path('displayroompage/<itemcatg>', views.displayroompage, name="displayroompage"),
    path('viewsingleroompage/<int:dataid>/',views.viewsingleroompage, name="viewsingleroompage"),
     path('savecustomerf/', views.savecustomerf, name="savecustomerf"),
    path('invoicef/', views.invoicef, name="invoicef"),

]