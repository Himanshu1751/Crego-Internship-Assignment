from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .models import Transaction
from .serializers import TransactionSerializer
import redis

r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class StatsView(APIView):
    def get(self, request):
        total_requests = int(r.get('api_request_count') or 0)
        total_transactions = Transaction.objects.count()
        return Response({
            "total_requests": total_requests,
            "total_transactions": total_transactions
        })
