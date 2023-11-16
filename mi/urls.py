from django.urls import path
from .views import *

app_name='vamsi'

urlpatterns=[

    path('rohit/',rohit,name='rohit'),
    path('bumrah/',bumrah,name='bumrah'),
]