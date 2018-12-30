from django.test import TestCase
from .models import Order

"""
    Test the views
"""


class TestViews(TestCase):
    # Test the checkout page
    def test_get_checkout_page(self):
        order = Order(full_name="Andrew Carton", phone_number="087645435", country="Ireland", postcode="Asdads", town_or_city="Drogheda", street_address1="My Steet", street_address2="My Street 2", county="County", date="2018-12-25")
        order.save()

        page = self.client.get("/checkout/{0}/checkout/".format(order.id))
        self.assertEqual(page.status_code, 302)
        