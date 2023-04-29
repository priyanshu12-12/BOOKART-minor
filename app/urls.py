from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('require', views.require, name='require'),
    path('purchase/<int:id>/', views.purchase, name='purchase'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)