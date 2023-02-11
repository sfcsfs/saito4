from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class XxxTestCase(TestCase):
    # HTTPステータスコードが405になるかどうか
    def test_response_405(self):
        x_url = reverse("cart_adds", kwargs={"product_id": 1})
        detail_response = self.client.get(x_url)
        self.assertEqual(detail_response.status_code, 405)
