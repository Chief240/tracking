from unicodedata import name
from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
path('', views.index, name='index'),
path('tracking/', views.tracking, name='tracking'),
path('error/', views.pagerror, name='error'),
path('tracking2/', views.tracking2, name='tracking2'),
path('error2/', views.pagerror2, name='error2'),
path('index2/', views.index2, name='index2'),
path('tracking_app_tablet/', views.tracking_app_tablet, name='tracking_app_tablet'),
path('major_services/', views.major_services, name='major_services'),
path('portfolio/', views.portfolio, name='portfolio'),
path('contact/', views.contact, name='contact'),
]