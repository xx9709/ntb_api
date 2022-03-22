from django.urls import path
from .views import AddUserView, GetMoneyView

urlpatterns = [    
    path('adduser', AddUserView.as_view()),
    path('getmoney', GetMoneyView.as_view()),
]