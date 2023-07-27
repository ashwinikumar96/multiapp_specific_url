from django.urls import path
from app1.views import *
app_name = 'app1'

urlpatterns = [
    path('p1/',p1,name='p1'),
    path('p2/',p2,name='p2'),
    path('string/',string,name='string'),
]