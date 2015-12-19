'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from unittest import mock
import unittest

from shellfash.controller.ProjectController import ProjectController
from shellfash.model.ProjectNameError import ProjectNameError


class TestProjectController(unittest.TestCase):
    '''
    Tests for ProjectName.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleFolder = mock.NonCallableMock()
        self.doubleFolder.create = mock.Mock()
        self.doubleFolder.delete = mock.Mock()
        self.doubleFolderClass = mock.Mock(return_value=self.doubleFolder)

        # Create instance of class under test.
        self.controller = ProjectController(
            _clsProjectFolder=self.doubleFolderClass
        )

    def test__createProject__create_not_called_for_invalid_name(self):
        try:
            self.controller.create_project('Invalid Name/@#')
        except:
            pass
        self.assertFalse(self.doubleFolder.create.called)

    def test__createProject__exception_thrown_for_invalid_name(self):
        self.assertRaises(
            excClass=ProjectNameError,
            callableObj=self.controller.create_project,
            projectNameString='Invalid Name/@#',
        )

    def test__createProject_and_deleteProject__create_and_delete_called_for_valid_name(self):
        self.controller.create_project('ValidName')
        self.doubleFolder.create.assert_called_once()
        self.controller.delete_project('ValidName')
        self.doubleFolder.delete.assert_called_once()

    def test__deleteProject__delete_not_called_for_invalid_name(self):
        try:
            self.controller.delete_project('Invalid Name/@#')
        except:
            pass
        self.assertFalse(self.doubleFolder.delete.called)

    def test__deleteProject__exception_thrown_for_invalid_name(self):
        self.assertRaises(
            excClass=ProjectNameError,
            callableObj=self.controller.delete_project,
            projectNameString='Invalid Name/@#',
        )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
