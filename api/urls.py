from django.urls import path
from .views import *

urlpatterns = [    
    path('add_user', AddUserView.as_view()),
]