
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.send_bulk_emails),
    #referal link 
    path('referal/',views.home_page),
    path('report/',views.report_page),
    path('referral/<str:referral_code>/', views.referral_redirect, name='referral_redirect'),
]
