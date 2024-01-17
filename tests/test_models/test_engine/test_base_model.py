import unittest
import os
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = storage

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass
        self.storage._FileStorage__objects = {}

    def test_all(self):
        base_model = BaseModel()
        new = storage.all()
        self.assertIsInstance(new, dict)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = storage
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())
        self.assertIsInstance(new_storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
