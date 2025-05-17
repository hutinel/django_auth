from .views import home, products, exit, register
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
]
