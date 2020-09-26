from django.urls import path

from garbage import views

urlpatterns = [
    path('details/',views.details),
    path('index/',views.index),
    path('get/',views.get)
]