from django.urls import path
from todoapp.views import MainPage

urlpatterns=[
  path('', MainPage, name='main-page')
]