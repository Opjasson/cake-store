from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.index),
    path('donuts/',include('donuts.urls')), 
    path('cake/',include('cake.urls')),
    path('pastry/',include('pastry.urls'))
]