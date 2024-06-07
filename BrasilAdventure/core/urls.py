from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('tours/', views.tours, name='tours'),
    path('bookings/', views.bookings, name='bookings'),
    path('about/', views.about, name='about'),
]
