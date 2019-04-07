from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Ramiro Júnior', cpf='12345678901',
                    email='ramirojunior@outlook.com', phone='21-99618-6180')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventexx.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventexx.com.br', 'ramirojunior@outlook.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ramiro Júnior',
            '12345678901',
            'ramirojunior@outlook.com',
            '21-99618-6180',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        

