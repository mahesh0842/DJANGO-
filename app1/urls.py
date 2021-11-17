from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,second,viewform,adduser,loginuser,submituser



urlpatterns = [
    path('',home,name= 'home page'),
    
    path('second',second ,name='second page'),
    path('form',viewform ,name='form'),
    path('adduser',adduser ,name='submituser'),
    path('loginuser',loginuser,name='loginuser'),
    path('submituser',submituser,name='submituser'),
]   
