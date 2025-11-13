from django.test import TestCase
from transactions.models import Transaction
from datetime import datetime

class TransactionModelTest(TestCase):
    def test_create_transaction(self):
        txn = Transaction.objects.create(
            amount=100.00,
            transaction_type='credit',
            description='Test transaction',
            transaction_time=datetime.now()
        )
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(str(txn), 'credit - 100.00')
