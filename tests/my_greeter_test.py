import unittest
from datetime import datetime
from unittest.mock import patch
from src.my_greeter import MyGreeter

class TestMyGreeter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting_returns_non_empty_string(self):
        greeting = self._my_greeter.greeting()
        self.assertTrue(len(greeting) > 0)

    def test_greeting_during_morning(self):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 6, 28, 8, 0, 0)  # 设置为早晨8点
            self.assertEqual(self._my_greeter.greeting(), "Good morning")

    def test_greeting_during_afternoon(self):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 6, 28, 14, 0, 0)  # 设置为下午2点
            self.assertEqual(self._my_greeter.greeting(), "Good afternoon")

    def test_greeting_during_evening(self):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value = datetime(2024, 6, 28, 20, 0, 0)  # 设置为晚上8点
            self.assertEqual(self._my_greeter.greeting(), "Good evening")

if __name__ == '__main__':
    unittest.main()

