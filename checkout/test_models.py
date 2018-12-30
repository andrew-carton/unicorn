from django.test import TestCase
from .models import Order
from datetime import datetime

class TestOrderModel(TestCase):
    def test_create_order_with_details(self):
        order = Order(full_name="Andrew Carton", phone_number="087645435", country="Ireland", postcode="Asdads", town_or_city="Drogheda", street_address1="My Steet", street_address2="My Street 2", county="County", date="2018-12-25")
        order.save()
        self.assertEquals(order.full_name, "Andrew Carton")
        self.assertEquals(order.phone_number, "087645435")
        self.assertEquals(order.country, "Ireland")
        self.assertEquals(order.postcode, "Asdads")
        self.assertEquals(order.town_or_city, "Drogheda")
        self.assertEquals(order.street_address1, "My Steet")
        self.assertEquals(order.street_address2, "My Street 2")
        self.assertEquals(order.county, "County")
        self.assertEquals(order.date, "2018-12-25")