from django.urls import path
from .views import user_list, user_detail, transaction_list, transaction_detail

urlpatterns = [    
    path('user', user_list),
    path('user_detail/<int:pk>', user_detail),
    path('transaction', transaction_list),
    path('transaction_detail/<int:pk>', transaction_detail),
] 