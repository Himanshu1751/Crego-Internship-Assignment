from django.urls import path
from .views import TransactionListCreateView, TransactionRetrieveUpdateDeleteView, StatsView

urlpatterns = [
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateDeleteView.as_view(), name='transaction-detail'),
    path('stats/', StatsView.as_view(), name='stats'),
]
