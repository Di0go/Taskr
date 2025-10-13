# ----------------------------------------------
# users/tests.py
# Tests for the users app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.test import TestCase
from .models import CustomUser
from django.urls import reverse


class AuthenticationTests(TestCase):

    # EN: Test a login with correct credentials
    def test_login_success(self):

        CustomUser.objects.create_user(username='testuser', password='pass123')
        response = self.client.post(reverse('users:login'), 
        {
            'username': 'testuser',
            'password': 'pass123',
        })

        self.assertRedirects(response, reverse('projects:index'))

    # EN: Test a login with incorrect credentials
    def test_login_fail(self):

        CustomUser.objects.create_user(username='testuser', password='pass123')
        response = self.client.post(reverse('users:login'), 
        {
            'username': 'testuser',
            'password': 'wrongpass',
        })

        # EN: Status Code 200 -> NO redirect 
        self.assertContains(response, "Please enter a correct username and password. Note that both fields may be case-sensitive.", status_code=200)


