from django.urls import path
from mobile.views import *
app_name='anything'

urlpatterns=[
    path('redmi/',redmi,name='redmi')
]