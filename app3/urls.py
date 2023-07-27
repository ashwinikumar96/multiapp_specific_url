from django.urls import path
from app3.views import *
app_name = 'app3'

urlpatterns = [
    path('p5/',p5,name='p5'),
    path('p6/',p6,name='p6'),
    path('string/',string,name='string'),
]