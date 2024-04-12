from django.urls import path
from .views import categories_view, category_view

urlpatterns = [
    path('categories', categories_view),
    path('categories/<int:pk>/', category_view)
]
