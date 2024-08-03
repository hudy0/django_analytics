from django.test import TestCase

from customers.models import Customer


class CustomerModelTests(TestCase):

    def setUp(self):
        # Create a Customer instance for use in tests
        self.customer = Customer.objects.create(
            name="Hudaifa Saleh", gender=Customer.MALE, age=30, favorite_number=7
        )

    def test_customer_creation(self):
        # Test that the customer is created with the correct values
        self.assertEqual(self.customer.name, "Hudaifa Saleh")
        self.assertEqual(self.customer.gender, Customer.MALE)
        self.assertEqual(self.customer.age, 30)
        self.assertEqual(self.customer.favorite_number, 7)
        self.assertIsNotNone(self.customer.created_at)  # created_at should be set

    def test_customer_str_method(self):
        # Test the __str__ method
        self.assertEqual(str(self.customer), "Hudaifa Saleh - M")

    def test_default_gender(self):
        # Test the default value of the gender field
        customer = Customer.objects.create(name="Default Gender", age=22, favorite_number=5)
        self.assertEqual(customer.gender, Customer.OTHER)
