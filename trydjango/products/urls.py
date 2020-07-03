from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view)

app_name = 'products'
urlpatterns = [
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list')
]
