from django.test import TestCase
from datetime import datetime

from eventexx.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ramiro Júnior',
            cpf='12345678901',
            email='ramirojunior@mailinator.com',
            phone='21-996166180'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Ramiro Júnior', str(self.obj))

