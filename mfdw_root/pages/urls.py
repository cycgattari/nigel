from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, {'pagename': ''} , name='home'),
    path('deptos', views.deptos, name='deptos'),
    path('contact', views.contact, name='contact'),
    path('mediciones', views.mediciones, name='mediciones'),
    path('<str:pagename>', views.index, name='index'),
]
