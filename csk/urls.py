from django.urls import path
from .views import *

app_name='vamsi'

urlpatterns=[

    path('dhoni/',dhoni,name='dhoni'),
    path('raina/',raina,name='raina'),
]