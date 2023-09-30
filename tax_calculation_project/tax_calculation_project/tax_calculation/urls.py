from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default'),
    path('<float:number>/', views.calculate_tax, name='calculate_tax'),
    path('taxrate/', views.tax_rate_view, name='tax_rate'),
]
