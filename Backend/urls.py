from django.urls import path
from Backend import views

urlpatterns = [

    path('', views.viewlogin, name="viewlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),


    path('indexpage/', views.indexpage, name="indexpage"),
    path('addadmin/', views.addadmin, name="addadmin"),
    path('saveadmin/', views.saveadmin, name="saveadmin"),
    path('viewadmin/', views.viewadmin, name="viewadmin"),
    path('editadmin/<int:dataid>/', views.editadmin, name="editadmin"),
    path('updateadmin/<int:dataid>/', views.updateadmin, name="updateadmin"),
    path('deleteadmin/<int:dataid>/', views.deleteadmin, name="deleteadmin"),
    path('viewmessage/', views.viewmessage, name="viewmessage"),
    path('deletemessage/<int:dataid>/', views.deletemessage, name="deletemessage"),

    path('addcustomer/', views.addcustomer, name="addcustomer"),
    path('savecustomer/', views.savecustomer, name="savecustomer"),
    path('viewcustomer/', views.viewcustomer, name="viewcustomer"),
    path('editcustomer/<int:dataid>/',views.editcustomer, name="editcustomer"),
    path('updatecustomer/<int:dataid>/', views.updatecustomer, name="updatecustomer"),
    path('deletecustomer/<int:dataid>/', views.deletecustomer, name="deletecustomer"),


    path('addroom/', views.addroom, name="addroom"),
    path('saveroom/', views.saveroom, name="saveroom"),
    path('viewroom/', views.viewroom, name="viewroom"),
    path('editroom/<int:dataid>/',views.editroom, name="editroom"),
    path('updateroom/<int:dataid>/', views.updateroom, name="updateroom"),
    path('deleteroom/<int:dataid>/', views.deleteroom, name="deleteroom"),


    path('addroomt/', views.addroomt, name="addroomt"),
    path('saveroomt/', views.saveroomt, name="saveroomt"),
    path('viewroomt/', views.viewroomt, name="viewroomt"),
    path('editroomt/<int:dataid>/',views.editroomt, name="editroomt"),
    path('updateroomt/<int:dataid>/', views.updateroomt, name="updateroomt"),
    path('deleteroomt/<int:dataid>/', views.deleteroomt, name="deleteroomt"),

]