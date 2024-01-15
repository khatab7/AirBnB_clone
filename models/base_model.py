#!/usr/bin/python3
"""class BaseModel defines all common attributes/methods for other classes"""
import uuid
import datetime
from models import storage


class BaseModel:
    """Base Class for all other Classes"""
    def __init__(self, *args, **kwargs):
        """Set up a new instance with a unique ID and timestamps."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """Get a readable string representation of the object's state."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the object."""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the object into a dictionary for storage or sharing."""
        dictionary = {}

        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
