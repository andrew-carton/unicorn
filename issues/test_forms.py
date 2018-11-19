from django.test import TestCase
from .forms import TicketForm, TicketFormEdit

class TestTicketForm(TestCase):

    def test_ticket_create(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : 'This is a description', 'type' : "HIGH", 'status' : "TODO", 'feature' : 'BUG', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertTrue(form.is_valid())

    def test_ticket_create_empty_title(self):
        form = TicketForm({'title' : '', 'description' : 'This is a description', 'type' : "HIGH", 'status' : "TODO", 'feature' : 'BUG', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

    def test_ticket_create_empty_description(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : '', 'type' : "HIGH", 'status' : "TODO", 'feature' : 'BUG', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])

    def test_ticket_create_empty_type(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : 'Test Descriptions', 'type' : "", 'status' : "TODO", 'feature' : 'BUG', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['type'], [u'This field is required.'])

    def test_ticket_create_empty_status(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : 'Test Description', 'type' : "HIGH", 'status' : "", 'feature' : 'BUG', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['status'], [u'This field is required.'])

    def test_ticket_create_empty_feature(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : 'Test Description', 'type' : "HIGH", 'status' : "TODO", 'feature' : '', 'created_by' : 'andrew', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['feature'], [u'This field is required.'])

    def test_ticket_create_empty_created_by(self):
        form = TicketForm({'title' : 'MyTestTicket', 'description' : 'test', 'type' : "HIGH", 'status' : "TODO", 'feature' : 'BUG', 'created_by' : '', 'created_on' : '2018-10-10', 'closed' : False, 'closed_by' : None, 'closed_on' : None})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['created_by'], [u'This field is required.'])



