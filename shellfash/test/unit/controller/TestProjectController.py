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
        self.doubleFolderClass = mock.Mock(return_value=self.doubleFolder)

        # Create instance of class under test.
        self.controller = ProjectController(
            _clsProjectFolder=self.doubleFolderClass
        )

    def test__createProject__create_called_for_valid_name(self):
        self.controller.createProject('ValidName')
        self.doubleFolder.assert_called_once()

    def test__createProject__create_not_called_for_invalid_name(self):
        try:
            self.controller.createProject('Invalid Name/@#')
        except:
            pass
        self.assertFalse(self.doubleFolder.called)

    def test__createProject__exception_thrown_for_invalid_name(self):
        self.assertRaises(
            excClass=ProjectNameError,
            callableObj=self.controller.createProject,
            projectNameString='Invalid Name/@#',
        )
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
