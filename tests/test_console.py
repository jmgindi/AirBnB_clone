#!/usr/bin/python3
"""Unit tests for comsole"""
import unittest
from console import HBNBCommand
from datetime import datetime
import json

class testsForConsole(unittest.TestCase):
    """Tests for comsole"""

    @classmethod
    def setUpClass(cls):
        """Prints that unit testing for console
        will commence!
        """
        print("\n...Testing for console...")

    def test_doc_string(self):
        """Tests doc string of console"""
        doc = ('console').__doc__
        self.assertIsNotNone(doc)

    def test_prompt(self):
        """Tests if the command prompt is correct"""
        a = HBNBCommand()
        self.assertEqual(a.prompt, "(hbnb) ")

    def test_do_quit_return_true(self):
        """Tests if quit returns correct value"""
        b = HBNBCommand()
        self.assertEqual(b.do_quit("quit"), True)

if __name__ == '__main__':
    unittest.main
