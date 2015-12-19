'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from unittest.mock import Mock, NonCallableMock
from shellfash.model.CommandRunner import CommandRunner


class TestCommandRunner(unittest.TestCase):
    '''
    Unit tests for CommandRunner.
    '''

    def setUp(self):
        # Create instance of class under test.
        self.runner = CommandRunner()

    def create_command_mocks(self):
        commands = []
        for i in range(2):
            commands.append(NonCallableMock())
            commands[i].run = Mock()
        return commands

    def test__runAll__runs_all_commands(self):
        commands = self.create_command_mocks()
        for command in commands:
            self.runner.add(command)
        self.runner.runAll()
        self.assertEqual(1, commands[0].run.call_count)
        self.assertEqual(1, commands[1].run.call_count)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
