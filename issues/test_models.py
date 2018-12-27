from django.test import TestCase
from .models import Ticket
from datetime import datetime

class TestTicketModel(TestCase):
    def test_create_ticket_with_name_and_datetime(self):
        ticket = Ticket(title="MyTicket", created_on=datetime.now())
        ticket.save()
        self.assertEquals(ticket.title, "MyTicket")

    def test_create_ticket_with_all(self):
        ticket = Ticket(title="MyTestTicket", description="My Test Ticket", type='LOW', status='TODO', feature='BUG', votes=0, created_by="andrew", created_on="2018-12-20", closed=True, closed_by="andrew", closed_on="2018-12-25")
        ticket.save()
        self.assertEquals(ticket.title, "MyTestTicket")
        self.assertEquals(ticket.description, "My Test Ticket")
        self.assertEquals(ticket.type, "LOW")
        self.assertEquals(ticket.status, "TODO")
        self.assertEquals(ticket.feature, "BUG")
        self.assertEquals(ticket.votes, 0)
        self.assertEquals(ticket.created_by, "andrew")
        self.assertEquals(ticket.created_on, "2018-12-20")
        self.assertEquals(ticket.closed, True)
        self.assertEquals(ticket.closed_by, "andrew")
        self.assertEquals(ticket.closed_on, "2018-12-25")
        