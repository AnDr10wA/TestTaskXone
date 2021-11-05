from django.contrib import admin
from django.urls import path, include
from .views import main_page, folow_link
urlpatterns = [

    path('<str:token>', folow_link),
    path('', main_page),

]