from django.contrib import admin
from django.urls import path, include
from .views import main_page, folow_link, user_links
urlpatterns = [
    path('links', user_links, name = 'links_user_url'),
    path('<str:token>', folow_link ),
    path('', main_page, name = 'main_page_url'),


]