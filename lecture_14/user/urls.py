from django.urls import path
from .views import login_page, register_page, handle_logout, profile_page_view, forgot_password_view, \
    reset_password_view

urlpatterns = [
    # products/
    path('login/', login_page, name='login-page'),
    path('register/', register_page, name='register-page'),
    path('logout/', handle_logout, name='logout'),
    path('settings/', profile_page_view, name='settings_page'),
    path('forgot-password/', forgot_password_view, name='forgot_password_page'),
    path('reset-password/<slug:token>', reset_password_view, name='reset_password_page'),
]
