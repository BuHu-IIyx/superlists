from django.test import TestCase


class SmokeTest(TestCase):
    '''Тест на токсичность'''

    def test_bad_maths(self):
        '''неправильные расчеты'''
        self.assertEqual(1 + 1, 3)
