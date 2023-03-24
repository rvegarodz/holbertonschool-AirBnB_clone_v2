import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    def test_create_no_arguments(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('create')
            self.assertEqual(output.getvalue(), "** class name missing **\n")

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('create InvalidClass')
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_show_no_arguments(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('show')
            self.assertEqual(output.getvalue(), "** class name missing **\n")
    
    def test_create_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('create BaseModel')
            obj_id = output.getvalue().strip()
            self.assertIsNotNone(storage.get('BaseModel', obj_id))

    def test_show_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('show InvalidClass 1234-5678')
            self.assertEqual(output.getvalue(), "** class doesn't exist **\n")

    def test_show_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('show BaseModel')
            self.assertEqual(output.getvalue(), "** instance id missing **\n")

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as output:
            console = HBNBCommand()
            console.onecmd('show BaseModel 1234-5678')
            self.assertEqual(output.getvalue(), "** no instance found **\n")

if __name__ == '__main__':
    unittest.main()
