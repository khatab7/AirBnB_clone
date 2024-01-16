import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        self.storage._FileStorage__objects = {}

    def test_all(self):
        base_model = BaseModel()
        user = User() # assuming User is a subclass of BaseModel
        expected_keys = {
            f"{base_model.__class__.__name__}.{base_model.id}",
            f"{user.__class__.__name__}.{user.id}",
            }
        self.storage.new(base_model)
        self.storage.new(user)
        self.storage.save()
        expected_keys = set(self.storage.all().keys())
        self.assertEqual(self.storage.all(), expected_keys)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())
        self.assertIsInstance(new_storage.all()[key], BaseModel)

if __name__ == '__main__':
    unittest.main()

