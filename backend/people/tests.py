from django.test import TestCase

from .models import People


class PersonTest(TestCase):
    def setUp(self):
        People.objects.create(name="Name1",
                              surname="Surname1",
                              telephone="123456789",
                              )
        People.objects.create(name="Name2",
                              surname="Surname2",
                              telephone="1234567890"
                              )

    def test_create_people(self):
        """People creation works correctly """
        person1 = People.objects.get(name="Name1")
        person2 = People.objects.get(name="Name2")

        self.assertEqual(person1.name, 'Name1')
        self.assertEqual(person1.surname, 'Surname1')
        self.assertEqual(person1.telephone, '123456789')
        self.assertEqual(person2.name, 'Name2')
        self.assertEqual(person2.surname, 'Surname2')
        self.assertEqual(person2.telephone, '1234567890')
