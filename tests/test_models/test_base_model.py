#!/usr/bin/python3
"""TestBaseModel test for BaseModel class."""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
import datetime

mock_time = datetime.datetime(2024, 1, 11, 10, 19, 18, 818094)


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""
    @classmethod
    def setUpClass(cls):
        """Setup class method to patch the time function."""
        cls.mock_time_patch = patch(
            'time.time',
            return_value=mock_time.timestamp())
        cls.mock_time_patch.start()

    @classmethod
    def tearDownClass(cls):
        """Teardown class method to stop the time patch."""
        cls.mock_time_patch.stop()

    def setUp(self):
        """Setup method to create a BaseModel instance."""
        self.base_model = BaseModel()

    def test_init(self):
        """Test case to check the initialization of BaseModel attributes."""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        """Test case to check the string representation of BaseModel."""
        out = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), out)

    def test_save(self):
        """Test case to check the save method of BaseModel."""
        mock_now = datetime.datetime(2024, 1, 11, 10, 19, 18, 818094)

        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_now

            ini_upd = self.base_model.updated_at
            self.base_model.save()

            self.assertGreaterEqual(self.base_model.updated_at, ini_upd)

    def test_to_dict(self):
        """Test case to check the to_dict method of BaseModel."""
        result = self.base_model.to_dict()

        self.assertIn('__class__', result)
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)
        self.assertEqual(result['__class__'], 'BaseModel')


if __name__ == '__main__':
    unittest.main()
