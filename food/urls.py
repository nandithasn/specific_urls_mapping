from django.urls import path
from food.views import *
app_name='something'

urlpatterns =[
    path('idli/',idli,name='idli')
]