from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_createUserWithEmailSuccessful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@test.com'
        password = 'test'
        user = get_user_model().objects.createUser(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_newUserEmailNormalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@TesT.COM'
        user = get_user_model().objects.createUser(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_newUserInvalidEmail(self):
        """Test creating user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.createUser(None, 'test123')

    def test_createNewSuperUser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.createSuperUser(
            'test@test.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

