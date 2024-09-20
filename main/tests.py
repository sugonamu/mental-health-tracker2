from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
          mood="Happy",
          time = now,
          feelings = "I'm happy, even though my clothes are soaked from the rain :(",
          mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)

    def test_main_using_main_template(self):
        # Log in the user and set the cookie
        self.client.login(username='testuser', password='12345')
        self.client.cookies['last_login'] = '2024-09-20T12:00:00Z'
        response = self.client.get('')
        self.assertTemplateUsed(response, 'main.html')