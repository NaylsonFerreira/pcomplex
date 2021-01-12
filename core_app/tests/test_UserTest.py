from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from core_app.models import Profile


class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'user_test@test.com',
            'email': 'user_test@test.com',
            'password': 'overloadLab100!',
            'password1': 'overloadLab100!',
            'password2': 'overloadLab100!'
        }

    # API Tests
    def test_singup_sucess(self):
        url = reverse('core_app:singup')
        response = self.client.post(url, self.credentials)
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username=self.credentials['username'])
        # Check if the profile has been created
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.email, self.credentials['username'])

        # Check if the token has been created
        Token.objects.get(user=user)

    def test_singup_invalid(self):
        # Invalid email
        invalid_credentials = self.credentials | {'username': 'invalid_email'}
        url = reverse('core_app:singup')
        response = self.client.post(url, invalid_credentials)
        self.assertEqual(response.status_code, 400)

        # Email has already been registered
        self.test_singup_sucess()

        url = reverse('core_app:singup')
        response = self.client.post(url, self.credentials)
        self.assertEqual(response.status_code, 400)

    def test_login_sucess(self):
        self.test_singup_sucess()

        url = reverse('core_app:login')
        response = self.client.post(url, self.credentials)
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username=self.credentials['username'])
        Token.objects.get(user=user)

    def test_login_invalid(self):
        # Unregistered user
        invalid_credentials = self.credentials | {
            'email': 'unregistered_user@test.com'}
        url = reverse('core_app:login')
        response = self.client.post(url, invalid_credentials)
        self.assertNotEqual(response.status_code, 302)

        # without credentials
        url = reverse('core_app:login')
        response = self.client.post(url, {})
        self.assertNotEqual(response.status_code, 302)
