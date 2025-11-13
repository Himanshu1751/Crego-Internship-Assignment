from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('debit', 'Debit'),
        ('credit', 'Credit'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    description = models.TextField()
    transaction_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"
