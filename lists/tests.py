from urllib import response
import django
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'hwome.html')
