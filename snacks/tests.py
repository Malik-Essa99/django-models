from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class TestSnacksList(TestCase):
    def test_status_code_snacks_list(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    def test_snacks_list_templates(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
