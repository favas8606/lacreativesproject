from django.urls import path
from . import views

app_name = 'lacreatives'

urlpatterns = [
    path('',views.index,name='index')
]

