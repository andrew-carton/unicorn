from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):

    def test_can_login_with_blank_password(self):
        form = UserLoginForm({'username' : 'Andrew', 'password' : ''})
        self.assertFalse(form.is_valid())

    def test_can_login_with_blank_username(self):
        form = UserLoginForm({'username' : '', 'password' : 'test'})
        self.assertFalse(form.is_valid())
    
    def test_can_login_with_blank_username_and_password(self):
        form = UserLoginForm({'username' : '', 'password' : ''})
        self.assertFalse(form.is_valid())

    def test_can_register(self):
        form = UserRegistrationForm({'email' : 'test@email.com', 'username' : 'myusername', 'password1' : 'mypass', 'password2' : 'mypass'})
        self.assertTrue(form.is_valid())

    def test_can_register_empty_email(self):
        form = UserRegistrationForm({'email' : '', 'username' : 'myusername', 'password1' : 'mypass', 'password2' : 'mypass'})
        self.assertEqual(form.errors['email'], [u'You must supply an email'])

    def test_can_register_empty_username(self):
        form = UserRegistrationForm({'email' : 'test@email.com', 'username' : '', 'password1' : 'mypass', 'password2' : 'mypass'})
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_mismatch_password(self):
        form = UserRegistrationForm({'email' : 'test@email.com', 'username' : 'myusername', 'password1' : 'mypass', 'password2' : 'mypass1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Password must match'])

