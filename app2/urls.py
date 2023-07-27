from django.urls import path
from app2.views import *
app_name = 'app2'

urlpatterns = [
    path('p3/',p3,name='p3'),
    path('p4/',p4,name='p4'),
    path('string/',string,name='string'),
]