from django.test import TestCase
from . import views
from django.urls import reverse
# Create your tests here.

class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)  # Проверка на равенство, сравнение левого и правого значения

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
                      response.content.decode())

    def test_signs(self):
        for i in views.zodiac_dict:
            reverse_path = reverse('zodiac_sign_url', args=('zodiac_sign', ))
            response = self.client.get(reverse_path)
            self.assertIn(views.zodiac_dict[i], response.content.decode())