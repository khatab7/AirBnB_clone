#!/usr/bin/env python3
"""Unittest module for base_model.py"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class Test_Base_Model(unittest.TestCase):
    """Test class for base_model"""

    def test_types(self):
        """Tests types of public instance attributes"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_id(self):
        """Tests id generation for BaseModel"""
        model = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model.id, model2.id)
        self.assertEqual(len(model.id), 36)

    def test_time(self):
        """Tests time attributes"""
        model = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model.created_at, model2.created_at)
        self.assertNotEqual(model.updated_at, model2.updated_at)

    def test_str(self):
        """Test str method"""
        model = BaseModel()
        string = f"[BaseModel] ({model.id}) {model.__dict__}"

    def test_to_dict(self):
        """Test to_dict method"""
        model = BaseModel()
        model.test_value = "School"
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertRegex(model_dict["test_value"], "School")

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        model_created = model.created_at
        model_updated = model.updated_at
        model.save()
        self.assertEqual(model_created, model.created_at)
        self.assertNotEqual(model_updated, model.updated_at)
