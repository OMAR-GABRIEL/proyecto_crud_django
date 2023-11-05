from django.urls import path
from . import views

urlpatterns=[
    path('',views.home ),
    path('insertempleado/',views.insertempleado),
    path('editEmpleado/<codigo>',views.editEmpleado),
    path('borrarEmpleado/<codigo>',views.borrarEmpleado),
    path('modificar/',views.modificar)
   

 ]
