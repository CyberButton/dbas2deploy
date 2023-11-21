"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from dbas2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Central CRUDS page
    path('cruds/', views.cruds, name='cruds'),

    # CRUD for Users
    path('cruds/user/', views.user_list, name='user_list'),
    path('cruds/user/create/', views.user_create, name='user_create'),
    path('cruds/user/update/<int:id>/', views.user_update, name='user_update'),
    path('cruds/user/delete/<int:id>/', views.user_delete, name='user_delete'),

    # CRUD for Caregivers
    path('cruds/caregiver/', views.caregiver_list, name='caregiver_list'),
    path('cruds/caregiver/create/', views.caregiver_create, name='caregiver_create'),
    path('cruds/caregiver/update/<int:id>/', views.caregiver_update, name='caregiver_update'),
    path('cruds/caregiver/delete/<int:id>/', views.caregiver_delete, name='caregiver_delete'),

    # CRUD for Members
    path('cruds/member/', views.member_list, name='member_list'),
    path('cruds/member/create/', views.member_create, name='member_create'),
    path('cruds/member/update/<int:id>/', views.member_update, name='member_update'),
    path('cruds/member/delete/<int:id>/', views.member_delete, name='member_delete'),

    # CRUD for Jobs
    path('cruds/job/', views.job_list, name='job_list'),
    path('cruds/job/create/', views.job_create, name='job_create'),
    path('cruds/job/update/<int:id>/', views.job_update, name='job_update'),
    path('cruds/job/delete/<int:id>/', views.job_delete, name='job_delete'),

    # CRUD for Job Applications
    path('cruds/jobapplication/', views.jobapplication_list, name='jobapplication_list'),
    path('cruds/jobapplication/create/', views.jobapplication_create, name='jobapplication_create'),
    path('cruds/jobapplication/update/<int:id>/', views.jobapplication_update, name='jobapplication_update'),
    path('cruds/jobapplication/delete/<int:id>/', views.jobapplication_delete, name='jobapplication_delete'),

    # CRUD for Appointments
    path('cruds/appointment/', views.appointment_list, name='appointment_list'),
    path('cruds/appointment/create/', views.appointment_create, name='appointment_create'),
    path('cruds/appointment/update/<int:id>/', views.appointment_update, name='appointment_update'),
    path('cruds/appointment/delete/<int:id>/', views.appointment_delete, name='appointment_delete'),

    # CRUD for Address
    path('cruds/address/', views.address_list, name='address_list'),
    path('cruds/address/create/', views.address_create, name='address_create'),
    path('cruds/address/update/<int:id>/', views.address_update, name='address_update'),
    path('cruds/address/delete/<int:id>/', views.address_delete, name='address_delete'),

    path('ping', views.ping_view, name='ping'),
]