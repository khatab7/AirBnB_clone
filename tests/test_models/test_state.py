#!/usr/bin/python3
"""Test State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State Class"""

    def test_state(self):
        """Test State Class"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

if __name__ == '__main__':
    unittest.main()