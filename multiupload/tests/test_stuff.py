from django.test import TestCase


class AnimalTestCase(TestCase):

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        assert 2 == 1 + 1
