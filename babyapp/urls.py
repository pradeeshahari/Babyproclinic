from django.urls import path
from .import views
app_name='babyapp'
urlpatterns=[

    path('c',views.indexhome,name='adminlogin'),
    path('adminportal',views.adminportal,name='portal'),
    path('doctorpanel',views.doctorpanel,name='panel'),
    path('doctoradd',views.adddoc,name='add'),
    path('update',views.updatedoc,name='update'),
    

    path('view',views.viewdoc,name='view'),
    path('master',views.master),
    path('p_contact',views.P_contact,name='contact'),
    path('m_delete/<int:mid>',views.deletecontact,name='m_delete'),

    path('i_delete/<int:iid>',views.deletedoctor,name='i_delete'),
    path('upt/<int:sid>',views.upt,name='s_update')
    



    
    
    

    



]