from django.urls import path
from .views import products_page_view, product_details_page_view, delete_product_page_view


urlpatterns = [
    # products/
    path('', products_page_view, name='products_page'),
    path('<int:pk>', product_details_page_view, name='product_details_page'),
    path('<int:pk>/delete', delete_product_page_view, name='delete_product_page')
]

