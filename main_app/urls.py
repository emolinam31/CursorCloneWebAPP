from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('pricing/', views.pricing, name='pricing'),
    path('download/', views.download, name='download'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
] 