from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterFormView

urlpatterns = [

    path('register/', RegisterFormView.as_view(), name='register'),

]
