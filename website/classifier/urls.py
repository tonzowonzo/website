from django.urls import path, include

from . import views

urlpatterns = [
    # Classifier home.
    path('', views.index, name='index'),
]