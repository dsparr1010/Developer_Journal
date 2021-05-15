from django.test import TestCase

class ExampleTestCase(TestCase):
    def setUp(self) -> None:
        self.example=True

    def test_01_example(self):
        self.assertEqual(self.example, True)