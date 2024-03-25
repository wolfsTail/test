from django.test import TestCase, Client
from django.urls import reverse

from main.forms import FileForm  

class IndexViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index')

    def test_index_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Загрузите текстовый файл')
        self.assertIsInstance(response.context['form'], FileForm)

    def test_index_post(self):
        import os

        with open('file.txt', 'wt', encoding='utf-8') as file:
            file.write("""Жила-была девушка по имени Брет,
                       шагала она быстрее, чем свет!""")
            
        with open('file.txt', 'rt', encoding='utf-8') as file:
            data = {'file': file}
            response = self.client.post(self.url, data, format='multipart')

        self.assertEqual(response.status_code, 200)
        self.assertTrue('frequency' in response.context)

        os.remove('file.txt')
