#!/usr/bin/python3
"""Review Test Class"""
from models.base_model import BaseModel
from models.review import Review
import unittest

class TestReview(unittest.TestCase):
    """Test Cases"""
    
    def test_review(self):
        """Test State Class"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)
        
    def test_attributes(self):
        """ """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")