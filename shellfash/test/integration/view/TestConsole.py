'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.view import console
from click.testing import CliRunner
import unittest

class TestConsole(unittest.TestCase):
    '''
    Integration tests for Console.
    '''

    def setUp(self):
        self.cliRunner = CliRunner()


    def test__path__echoes_lengthy_string(self):
        result = self.cliRunner.invoke(console.path)
        self.assertEqual(0, result.exit_code)
        self.assertGreater(len(result.output), 8)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
