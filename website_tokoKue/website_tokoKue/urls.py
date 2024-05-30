from.import view
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('about/',include('about.urls')),
]
