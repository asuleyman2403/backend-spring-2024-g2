from django.urls import path
from .views import index_page, products_details, delete_product


urlpatterns = [
    # products/
    path('', index_page),
    path('<int:pk>', products_details),
    path('<int:pk>/delete', delete_product)
]

