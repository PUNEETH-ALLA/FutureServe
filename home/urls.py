from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/<str:service_name>/', views.service_detail, name='services_detail'),
    path('careers/', views.careers, name='careers'),
    path('careers/<str:job_title>/', views.career_detail, name='career_detail'),  # <-- Added Career Details Route
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('industries/', views.industries, name='industries'),
]
