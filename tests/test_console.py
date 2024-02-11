import unittest
from unittest.mock import patch
from console import HBNBConsole

class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBConsole()

    def tearDown(self):
        pass

    def test_prompt(self):
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_EOF(self):
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.console.do_EOF(''))

    def test_do_help(self):
        with patch('builtins.input', return_value='help'):
            self.assertTrue(self.console.do_help(''))

    def test_do_quit(self):
        with patch('builtins.input', return_value='quit'):
            self.assertTrue(self.console.do_quit(''))

    def test_emptyline(self):
        self.assertIsNone(self.console.emptyline())

if __name__ == '__main__':
    unittest.main()import unittest
from unittest.mock import patch
from console import HBNBConsole

class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBConsole()

    def tearDown(self):
        pass

    def test_prompt(self):
        self.assertEqual(self.console.prompt, '(hbnb) ')

    def test_do_EOF(self):
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.console.do_EOF(''))

    def test_do_help(self):
        with patch('builtins.input', return_value='help'):
            self.assertTrue(self.console.do_help(''))

    def test_do_quit(self):
        with patch('builtins.input', return_value='quit'):
            self.assertTrue(self.console.do_quit(''))

    def test_emptyline(self):
        self.assertIsNone(self.console.emptyline())

    def test_do_create(self):
        with patch('builtins.input', return_value='create BaseModel'):
            self.console.do_create('')
            # Add assertions to check if the object was created and saved correctly

    def test_do_show(self):
        with patch('builtins.input', return_value='show BaseModel 123'):
            self.console.do_show('')
            # Add assertions to check if the correct instance was shown

    def test_do_destroy(self):
        with patch('builtins.input', return_value='destroy BaseModel 123'):
            self.console.do_destroy('')
            # Add assertions to check if the correct instance was destroyed

    def test_do_all(self):
        with patch('builtins.input', return_value='all'):
            self.console.do_all('')
            # Add assertions to check if all instances were printed

    def test_do_update(self):
        with patch('builtins.input', return_value='update BaseModel 123 name "New Name"'):
            self.console.do_update('')
            # Add assertions to check if the attribute was updated correctly

if __name__ == '__main__':
    unittest.main()