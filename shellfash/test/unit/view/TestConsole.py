'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from click.testing import CliRunner
from unittest import mock
import unittest

from shellfash.controller.ProjectController import ProjectController
from shellfash.view import console


class TestConsole(unittest.TestCase):
    '''
    Unit tests for Console.
    '''

    def setUp(self):
        # Create test doubles.
        self.doubleProjectController = mock.NonCallableMock(
            spec=ProjectController()
        )
        self.doubleProjectController.createProject = mock.Mock()
        console._setDependencies(
            projectController=self.doubleProjectController
        )

        self.cliRunner = CliRunner()

    def tearDown(self):
        console._setDependencies()

    def test__new__success_exit_code(self):
        result = self.cliRunner.invoke(console.new, ['Test'])
        self.assertEqual(0, result.exit_code)

    def test__new__success_message(self):
        result = self.cliRunner.invoke(console.new, ['Test'])
        self.assertTrue(result.output.startswith('Project created.'))

    def test__new__error_exit_code(self):
        self.doubleProjectController.createProject.side_effect = OSError
        result = self.cliRunner.invoke(console.new, ['Test'])
        self.assertNotEqual(0, result.exit_code)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
