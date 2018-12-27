from django.test import TestCase
from .models import Ticket

"""
    Test the views
"""


class TestViews(TestCase):
    # Test the bugs page
    def test_get_bugs_page(self):
        page = self.client.get("/issues/bugs")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bugs.html")

    # Test the features page
    def test_get_features_page(self):
        page = self.client.get("/issues/features")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "features.html")

    # Test the features page
    def test_get_createticket_page(self):
        page = self.client.get("/issues/createticket")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticketform.html")

    # Test the edit page
    def test_get_edit_page(self):
        ticket = Ticket(title="TestTicket")
        ticket.save()

        page = self.client.get("/issues/{0}/edit/".format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "ticketform.html")

    def test_get_bug_page(self):
        ticket = Ticket(title="TestTicket")
        ticket.save()

        page = self.client.get("/issues/{0}/bug/".format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug.html")

    def test_get_feature_page(self):
        ticket = Ticket(title="TestTicket")
        ticket.save()

        page = self.client.get("/issues/{0}/feature/".format(ticket.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature.html")