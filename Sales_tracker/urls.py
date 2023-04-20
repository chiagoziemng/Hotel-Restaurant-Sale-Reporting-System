from django.urls import path
from . import views

urlpatterns = [
    path('add_sale/', views.add_sale, name='add_sale'),
    path('view_sales/', views.view_sales, name='view_sales'),
    path('manage_inventory/', views.manage_inventory, name='manage_inventory'),
    path('manage_staff/', views.manage_staff, name='manage_staff'),
]
