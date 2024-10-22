from django.urls import path
from . import views

urlpatterns = [
    path('install/', views.site_install),
]
