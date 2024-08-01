from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.webpage1, name='webpage1'),
    path('login', views.webpage2, name='webpage2'),
    path('form', views.webpage3, name='webpage3'),
    path('receiving.html', views.receiving, name='receiving'),  # Add this line
]
