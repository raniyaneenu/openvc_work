from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('red',views.red_det,name='red'),
    path('blue',views.blue_det,name='blue'),
    path('green',views.green_det,name='green')

]