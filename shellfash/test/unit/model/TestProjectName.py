'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from unittest import mock
from shellfash.model.ProjectName import ProjectName
from shellfash.model.ProjectNameValidator import ProjectNameValidator
from shellfash.model.ProjectNameError import ProjectNameError

class TestProjectName(unittest.TestCase):
    '''
    Tests for ProjectName.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleNameValidator = mock.NonCallableMock(
            spec = ProjectNameValidator()
        )
    
        # Create instance of class under test.
        self.projectName = ProjectName(
            projectNameString = 'shellfash',
            _nameValidator = self.doubleNameValidator,
        )
    
    
    def test_constructor_projectNameString_good_verify_no_exception(self):
        self.doubleNameValidator.validate = mock.Mock(return_value=True)
        self.projectName = ProjectName(
            projectNameString = 'GoodName',
            _nameValidator = self.doubleNameValidator
        )
    
    def test_constructor_projectNameString_bad_verify_exception(self):
        self.doubleNameValidator.validate = mock.Mock(return_value=False)
        self.assertRaises(
            excClass = ProjectNameError,
            callableObj = ProjectName,
            projectNameString = 'Bad/Name',
            _nameValidator = self.doubleNameValidator
        )


    def test__get_full_name__verify_return_is_from_constructor_argument(self):
        self.doubleNameValidator.validate = mock.Mock(return_value=True)
        self.projectName = ProjectName(
            projectNameString = 'TestName',
            _nameValidator = self.doubleNameValidator
        )
        self.assertEqual("TestName", self.projectName.get_full_name())

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
