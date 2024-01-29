from django.urls import path
from .views import index_page, products_details


urlpatterns = [
    # products/
    path('', index_page),
    path('<int:pk>', products_details)
]

