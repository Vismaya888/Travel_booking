from django.urls import path,include
from . import views
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.Log_in,name='login'),
    path('logout/',views.log_out,name='logout')
]
