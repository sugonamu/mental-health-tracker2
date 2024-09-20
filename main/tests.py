from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import MoodEntry

class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='11111')

    def test_main_url_exists(self):
        # Log in the user and set the cookie
        self.client.login(username='tester', password='11111')
        self.client.cookies['last_login'] = '2024-09-20T12:00:00Z'  # Example timestamp
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        # Log in the user and set the cookie
        self.client.login(username='tester', password='11111')
        self.client.cookies['last_login'] = '2024-09-20T12:00:00Z'
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = self.client.get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
            user=self.user,  # Ensure mood entry is associated with the test user
            mood="Happy",
            time=now,
            feelings="I'm happy, even though my clothes are soaked from the rain :(",
            mood_intensity=8,
        )
        self.assertTrue(mood.is_mood_strong)

    def test_main_template_uses_correct_page_title(self):
        # Log in the user and set the cookie
        self.client.login(username='tester', password='11111')
        self.client.cookies['last_login'] = '2024-09-20T12:00:00Z'
        response = self.client.get("/")
        html_response = response.content.decode("utf8")
        self.assertIn("My Application", html_response)