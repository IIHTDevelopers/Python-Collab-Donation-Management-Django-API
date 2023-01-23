"""DonationManagenemtAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from donationapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('ngo/',views.NGOView.as_view()),
    path('ngo_pk/<int:pk>/',views.NGOView.as_view()),

    path('donar/',views.DonorView.as_view()),
    path('donar_pk/<int:pk>/',views.DonorView.as_view()),
    path('donar_ngo_pk/<int:pk>/',views.DonorWithNGOView.as_view()),

    path('donation/',views.DonationView.as_view()),
    path('donation_pk/<int:pk>/',views.DonationView.as_view()),
    path('donation_donar_pk/<int:pk>/',views.DonationByDonarView.as_view()),
    path('donation_ngo_pk/<int:pk>/',views.DonationForNGOView.as_view()),

    path('donation_request/',views.DonationRequestView.as_view()),
    path('donation_request_donar_pk/<int:pk>/',views.DonationRequestView.as_view()),
    path('donation_request_ngo_pk/<int:pk>/',views.DonationRequestByNGOView.as_view())
]
