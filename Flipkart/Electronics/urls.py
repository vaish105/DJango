from django.urls import path
from . import views 

urlpatterns = [
    path('edit/<int:id>/', views.edit_product, name='edit_product'),  # Corrected view name and parameter
]