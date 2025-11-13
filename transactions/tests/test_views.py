from django.urls import reverse
from rest_framework.test import APITestCase
from transactions.models import Transaction
from datetime import datetime

class TransactionViewTests(APITestCase):
    def setUp(self):
        self.transaction = Transaction.objects.create(
            amount=50.00,
            transaction_type='debit',
            description='Sample',
            transaction_time=datetime.now()
        )

    def test_list_transactions(self):
        response = self.client.get(reverse('transaction-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_transaction(self):
        data = {
            "amount": 75.00,
            "transaction_type": "credit",
            "description": "New",
            "transaction_time": datetime.now().isoformat()
        }
        response = self.client.post(reverse('transaction-list'), data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_retrieve_transaction(self):
        response = self.client.get(reverse('transaction-detail', args=[self.transaction.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_transaction(self):
        response = self.client.delete(reverse('transaction-detail', args=[self.transaction.id]))
        self.assertEqual(response.status_code, 204)
