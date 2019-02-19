#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""Unit tests for base model"""

class testBaseModelInit(unittest.TestCase):
    """Tests for BaseModel init function"""

    def test_args(self):
        base = BaseModel(1)
        self.assertNotEqual(base.id, 1)

    def test_kwargs_id(self):
        base = BaseModel(id="435-90312-cb4871")
        self.assertEqual(base.id, "435-90312-cb4871")

    def test_kwargs_casts_id(self):
        base = BaseModel(id=41571)
        self.assertEqual(type(base.id), str)

    def test_kwargs_created_at(self):
        """Tests that created_at is copied to object loaded
        from file"""

    def test_kwargs_updated_at(self):
        """Tests that updated_at is copied to loaded object"""

    def test_


class testBaseModelMethods(unittest.TestCase):
    """Tests for BaseModel"""

    def setUp(self):
        """setUp method creates an instance of BaseModel"""
        base = BaseModel()
        base_id = BaseModel.id

    def tearDown(self):
        """tearDown method deletes the BaseModel and
        updates filesystem"""
        del base

    def test_id(self):
        """Tests that uuids are unique"""
        base_y = BaseModel()
        self.assertNotEqual(base_y.id, self.base_id)

    def test_created_at_is_updated_at(self):
        """Tests that initial created_at and updated_at are equal"""
        self.assertEqual(self.base.created_at, self.base.updated_at)

    def test_str_class(self):
        """Tests str printing class name correctly"""

    def test_str_id(self):
        """Tests str printing id correctly"""

    def test_str_dict(self):
        """Tests str printing dict correctly"""

    def test_save_updates_updated_at(self):
        """Tests that save updates updated_at"""

    def test_save_no_file(self):
        """Tests that save works with no file"""

    def test_save_empty_file(self):
        """Tests that save works on an empty file"""

    def test_save_file_has_objects(self):
        """Tests that save works on a file that already contains
        other BaseModels"""

    def test_to_dict(self):
        """Tests that the to_dict method works"""

if __name__ == "__main__":
    testBaseModel()
