from unittest import TestCase

from factory.src.factory import Company


class FactoryTest(TestCase):
    """
        Test for checking Factory Design Pattern
        """
    
    def test_check_creating_mutiple_object(self):
        """
            Check if created similar objects
            """
        obj_1 = Company.factory("Google")
        obj_2 = Company.factory("Google")
        self.assertEqual(type(obj_1), type(obj_2))
    
    def test_can_create_different_objects(self):
        """
            Check objects of different types
            """
        obj_1 = Company.factory("Google")
        obj_2 = Company.factory("Apple")
        self.assertFalse(obj_1 is obj_2)
    
    def test_bad_creation_of_object(self):
        """
            Check bad creating of object
            """
        obj = Company.factory("ZeroToOneLabs")
        self.assertRaises(TypeError, obj)
