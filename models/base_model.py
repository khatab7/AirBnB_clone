#!/usr/bin/python3
"""class BaseModel defines all common attributes/methods for other classes"""
import uuid
import datetime


class BaseModel:
    """Base Class for all other Classes"""

    def __init__(self):
        """Set up a new instance with a unique ID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Get a readable string representation of the object's state."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the object."""
        update_at = datetime.datetime.now()

    def to_dict(self):
        """Convert the object into a dictionary for storage or sharing."""
        obj = self.__dict__.copy()

        obj['__class__'] = self.__class__.__name__

        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
