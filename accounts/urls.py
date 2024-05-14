from django.contrib import admin
from django.urls import path, include
from accounts.views import *


urlpatterns = [
    path('home/', homepage, name = 'homepage'),
    path('signup/', signup, name = 'signup'),
    path('login/', signin, name = 'login'),
    path('logout/', logout_view, name = "logout")
]