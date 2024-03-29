from django.urls import path
from .views import login_page_view, register_page_view, handle_logout, settings_page_view

urlpatterns = [
    path('login/', login_page_view, name='login'),
    path('register/', register_page_view, name='register'),
    path('logout/', handle_logout, name='logout'),
    path('settings/', settings_page_view, name='settings_page')
]
