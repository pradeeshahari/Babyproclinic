from django.urls import path
from .import views
app_name='doctorapp'
urlpatterns=[
    path('login',views.doctorlogin,name='log'),
    path('doctorappointment',views.appointment,name='appoint'),
    path('patientlist',views.list,name='list'),
    path('l_delete/<int:lid>',views.deletelist,name='l_delete'),
    path('x_delete/<int:xid>',views.deletebooking,name='x_delete'),
    path('statusupdte/<int:xid>',views.status_update,name='status_update'),
    path('masterpage',views.master),


]