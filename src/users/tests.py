# ----------------------------------------------
# users/tests.py
# Tests for the users app
# 
# <diogopinto> 2025+
# ----------------------------------------------

from django.test import TestCase
from .models import CustomUser
from django.urls import reverse



# EN: Tests for the login action 
class LoginTests(TestCase):

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



# EN: Tests for the register action
class RegisterTests(TestCase):
    # EN: Test a correct register
    def test_register_success(self):

        response = self.client.post(reverse('users:register'),
        {
            'username': 'newuser',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        })

        # EN: Confirm test by seeing if the successful register redirects to the login page
        self.assertRedirects(response, reverse('users:login'))

        self.assertTrue(CustomUser.objects.filter(username='newuser').exists())

    # EN: Test an incorrect register (password1 and password2 mismatch)
    def test_register_mismatch(self):

        response = self.client.post(reverse('users:register'),
        {
            'username': 'mismatchuser',
            'password1': 'StrongPassword123',
            'password2': 'WrongPassword123!',
        })

        # EN: Status Code 200 -> NO redirect 
        self.assertContains(response, "The two password fields didn’t match.", status_code=200)
    
    # EN: Test an incorrect register (username already exists)
    def test_register_username_already_exists(self):

        CustomUser.objects.create_user(username='existinguser', password='pass123')

        response = self.client.post(reverse('users:register'),
        {
            'username': 'existinguser',
            'password1': 'StrongPassword123!',
            'password2': 'StrongPassword123!',
        })

        # EN: Status Code 200 -> NO redirect 
        self.assertContains(response, "A user with that username already exists.", status_code=200)



# EN: Tests for the avatar field in the users/models.py
class AvatarTests(TestCase):

# TODO: Fazer os testes

    def test_avatar_size(self):
        self.assertTrue(True)

    def test_avatar_file_type(self):
        self.assertTrue(True)
