from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/update', views.CustomerUpdateView.as_view(), name='customer-update'),
    path('<int:pk>/delete', views.CustomerDeleteView.as_view(), name='customer-delete')
]