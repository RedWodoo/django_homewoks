from django.urls import path
from .views import ProductListView, add_product

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('add/', add_product, name='add_product'),

]