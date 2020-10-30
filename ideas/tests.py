from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from django.test import TestCase

# Create your tests here.
User = get_user_model()
class AccountTestCase(TestCase):
    """
    
    Performs account related tests.

    * user_exists
    * user_password
    * login_URL

    """

    # Initial method to prepare test
    def setUp(self):
        # Create test user
        user_a = User(username="test_user", email='test_user@test.com')
        user_a.is_staff = True
        user_a.is_superuser = True        
        user_a_pw = "test_user_password_123"                
        user_a.set_password(user_a_pw)
        user_a.save()
        
        self.user_a = user_a
        self.user_a_pw = user_a_pw
    

    def test_user_exists(self):
        # Count all users
        user_count = User.objects.all().count()

        # User count should be equal to 1
        self.assertEqual(user_count, 1)

        # User count should NOT be equal to 0
        self.assertNotEqual(user_count, 0)


    def test_user_password(self):
        user_a = User.objects.get(username="test_user")                

        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )


    def test_login_url(self):
        # Login url from settings
        login_url = settings.LOGIN_URL

        # Test data
        data = {"username": "test_user", "password": "test_user_password_123"}

        # Login with testdata and assign to responce object
        response = self.client.post(login_url, data, follow=True)

        # Get HTTP status code from response object        
        status_code = response.status_code
        
        # Set redirect_path to "default" path 
        redirect_path = response.request.get("PATH_INFO")
        
        # User should be redirected to the LOGIN_REDIRECT_URL defined in the settings file.
        self.assertEqual(redirect_path, settings.LOGIN_REDIRECT_URL)

        # HTTP Status Code 200 means "OK"
        self.assertEqual(status_code, 200)