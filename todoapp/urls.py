from django.urls import path
from todoapp.views import MainPage, Lists

urlpatterns=[
  path('', MainPage, name='main-page'),
  path('<str:list_name>', Lists, name='list')
]