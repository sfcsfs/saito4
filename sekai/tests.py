from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class XxTestCase(TestCase):
    # HTTPステータスコードが２００になるかどうか
    def test_response_200(self):
        x_url = reverse("w:kennsakus")
        detail_response = self.client.get(x_url)
        self.assertEqual(detail_response.status_code, 200)
