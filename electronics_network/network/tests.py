import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electronics_network.settings')
import django
django.setup()

from django.test import TestCase
from .models import Address, NetworkUnit, Product


class AddressModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            country="Россия",
            city="Москва",
            street="Тверская",
            building_number="12"
        )

    def test_address_str(self):
        address = self.address
        self.assertEqual(str(address), "Россия, Москва, Тверская 12")

    def test_address_fields(self):
        address = self.address
        self.assertEqual(address.country, "Россия")
        self.assertEqual(address.city, "Москва")
        self.assertEqual(address.street, "Тверская")
        self.assertEqual(address.building_number, "12")


class NetworkUnitModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            country="Россия",
            city="Москва",
            street="Тверская",
            building_number="12"
        )
        cls.network_unit = NetworkUnit.objects.create(
            name="Test Network Unit",
            contact_email="test@example.com",
            address=cls.address,
            debt=100.00
        )

    def test_network_unit_str(self):
        network_unit = self.network_unit
        self.assertEqual(str(network_unit), "Test Network Unit")

    def test_network_unit_fields(self):
        network_unit = self.network_unit
        self.assertEqual(network_unit.name, "Test Network Unit")
        self.assertEqual(network_unit.contact_email, "test@example.com")
        self.assertEqual(network_unit.address, self.address)
        self.assertEqual(network_unit.debt, 100.00)

    def test_supplier_foreign_key(self):
        supplier_network_unit = NetworkUnit.objects.create(
            name="Supplier Network Unit",
            contact_email="supplier@example.com",
            address=self.address,
            debt=200.00
        )
        self.network_unit.supplier = supplier_network_unit
        self.network_unit.save()

        network_unit = NetworkUnit.objects.get(id=self.network_unit.id)
        self.assertEqual(network_unit.supplier, supplier_network_unit)


class ProductModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.address = Address.objects.create(
            country="Россия",
            city="Москва",
            street="Тверская",
            building_number="12"
        )
        cls.network_unit = NetworkUnit.objects.create(
            name="Test Network Unit",
            contact_email="test@example.com",
            address=cls.address,
            debt=100.00
        )
        cls.product = Product.objects.create(
            name="Test Product",
            model="Model 1",
            release_date="2024-01-01"
        )
        cls.product.suppliers.add(cls.network_unit)

    def test_product_str(self):
        product = self.product
        self.assertEqual(str(product), "Test Product (Model 1)")

    def test_product_fields(self):
        product = self.product
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.model, "Model 1")
        self.assertEqual(product.release_date, "2024-01-01")

    def test_product_suppliers(self):
        product = self.product
        self.assertIn(self.network_unit, product.suppliers.all())