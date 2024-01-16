#!/usr/bin/python3
"""Amenity Test Class"""
from models.base_model import BaseModel
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Test Cases"""

    def test_amenity(self):
        """Test Amenity Class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """ """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
