from django.urls import path, include

from . import views

urlpatterns = [
    # CONTACT home.
    path('', views.contact, name='contact'),
]