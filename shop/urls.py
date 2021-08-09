
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customerProducts/', views.customerProducts, name='customerProducts'),
    path('customerProducts/<str:pk>/', views.order_details, name='details'),

    path('categories/<str:pk>/', views.categoryList, name="categories"),
    path('categories/<str:pk>/<str:sk>/', views.subcategoryList, name="subcategories"),
]
