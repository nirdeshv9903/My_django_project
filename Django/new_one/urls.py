from django.contrib import admin
from django.urls import path
from new_one import views

urlpatterns = [
    path('',views.index, name="new_one"),
    path('login/',views.login_u, name="login"),
    path('logout/',views.logout_u, name="logout"),
    path('create/',views.create, name="create"),
    path('singin/',views.singin, name="singin"),
]
