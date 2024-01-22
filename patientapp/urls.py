from django.urls import path
from .import views
app_name='patientapp'
urlpatterns=[
    path('',views.clinichome,name='home'),
    path('patientbooking',views.booking,name='booking'),
    path('view',views.signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('master',views.master),
    path('about',views.aboutus,name='about'),
    path('contact',views.contact,name='contact'),
    path('contact',views.contact,name='contact'),
    path('bookingstatus',views.bookingstatus,name='bookingstatus'),
    
    
    
]                       