import unittest
from unittest.mock import patch

import stupid

class TestStupid(unittest.TestCase) :
    @patch('builtins.input', side_effect=["what", "what", "soft"])
    def test_soft_n3(self, mock_input) :
    '''OK'''
        stupid.StupidDialog().dialog()
        self.assertEqual(mock_input.call_count, 3)
    @patch('builtins.input', side_effect=["what", "what", "smart"])
    def test_smart_n3(self, mock_input) :
    '''OK'''
        stupid.StupidDialog().dialog()
        self.assertEqual(mock_input.call_count, 3)
    @patch('builtins.input', side_effect=["what", "what", "hard"])
    def test_hard_n3(self, mock_input) :
    '''not OK because of exit'''
        stupid.StupidDialog().dialog()
        self.assertEqual(mock_input.call_count, 3)
    @patch('builtins.input', side_effect=["what", "what", "hard"])
    @patch('sys.exit')
    def test_hard_exit(self, mock_exit, mock_input) :
    '''OK'''
        try:
            with self.assertRaises(SystemExit):
                stupid.StupidDialog().dialog()
        except StopIteration:
            pass
        mock_exit.assert_called_once_with(1)
    @patch('builtins.input', side_effect=["what", "what", "hard"])
    @patch('sys.exit')
    def test_hard_exit_n3(self, mock_exit, mock_input) :
    '''not OK because of call_count'''
        try:
            with self.assertRaises(SystemExit):
                stupid.StupidDialog().dialog()
        except StopIteration:
            pass
        mock_exit.assert_called_once_with(1)
        self.assertEqual(mock_input.call_count, 3)

if __name__ == '__main__' :
    unittest.main()
