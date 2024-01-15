#!/usr/bin/python3
"""Test Class User"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Unit tests for the User class"""

    def setUp(self):
        """Setup method to create a User instance."""
        self.user = User()
        self.user.first_name = "maaz"
        self.user.last_name = "alside"
        self.user.email = "m@gmail.com"
        self.user.password = "1234"

    def test_init(self):
        """Test Cases for init method."""
        self.assertEqual(self.user.first_name, "maaz")
        self.assertEqual(self.user.last_name, "alside")
        self.assertEqual(self.user.email, "m@gmail.com")
        self.assertEqual(self.user.password, "1234")


if __name__ == "__main__":
    unittest.main()
