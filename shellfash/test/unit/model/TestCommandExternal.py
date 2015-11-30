'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from unittest import mock
import unittest
from shellfash.model.CommandExternal import CommandExternal


class TestCommandExternal(unittest.TestCase):
    '''
    Unit tests for CommandExternal.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleSubprocess = mock.NonCallableMock()
        self.doubleSubprocess.call = mock.Mock()

        # Create instance of class under test.
        self.command = CommandExternal(
            commandString='test',
            _subprocess=self.doubleSubprocess
        )

    def test__run__returns_the_exit_code_from_call(self):
        self.doubleSubprocess.call.return_value = 42
        result = self.command.run()
        self.assertEqual(42, result)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
