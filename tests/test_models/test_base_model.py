import unittest
from unittest.mock import patch, Mock
from models.base_model import BaseModel
import datetime

mock_time = datetime.datetime(2024, 1, 11, 10, 19, 18, 818094)

class TestBaseModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.mock_time_patch = patch('time.time', return_value=mock_time.timestamp())
        cls.mock_time_patch.start()

    @classmethod
    def tearDownClass(cls):
        cls.mock_time_patch.stop()
    def setUp(self):
        self.base_model = BaseModel()

    def test_init(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str(self):
        expected_string = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_string)

    def test_save(self):
        mock_now = datetime.datetime(2024, 1, 11, 10, 19, 18, 818094)

        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = mock_now

            initial_updated_at = self.base_model.updated_at
            self.base_model.save()

            self.assertGreaterEqual(self.base_model.updated_at, initial_updated_at)

    def test_to_dict(self):
        result = self.base_model.to_dict()

        self.assertIn('__class__', result)
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)
        self.assertEqual(result['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()

