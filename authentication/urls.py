from django.urls import path
from .views import *

urlpatterns = [
    path('auth/signup/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('categories/', ExpenseCategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', ExpenseCategoryDetailAPIView.as_view(), name='category-detail'),
    path('expenses/', ExpenseListCreateAPIView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailAPIView.as_view(), name='expense-detail'),
]