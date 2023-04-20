from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import InventoryItem, StaffMember

class InventoryItemTestCase(TestCase):
    def setUp(self):
        self.item = InventoryItem.objects.create(name='Test Item', quantity=5, reorder_level=3)

    def test_str_method(self):
        self.assertEqual(str(self.item), 'Test Item')

    def test_get_absolute_url_method(self):
        url = reverse('inventory_item_detail', args=[str(self.item.id)])
        self.assertEqual(self.item.get_absolute_url(), url)

class StaffMemberTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.staff_member = StaffMember.objects.create(user=self.user, role='MANAGER')

    def test_str_method(self):
        self.assertEqual(str(self.staff_member), 'testuser - MANAGER')

