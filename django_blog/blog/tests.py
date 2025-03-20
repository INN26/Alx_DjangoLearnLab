from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthenticationTestCase(TestCase):

    def setUp(self):
        """Create a test user"""
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_registration_page(self):
        """Test if the registration page loads"""
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Test if the login page loads"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_user_registration(self):
        """Test user registration process"""
        response = self.client.post('/accounts/register/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        """Test user login with valid credentials"""
        response = self.client.post('/accounts/login/', {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_invalid_login(self):
        """Test user login with invalid credentials"""
        response = self.client.post('/accounts/login/', {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        """Test user logout"""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)  # Should redirect after logout