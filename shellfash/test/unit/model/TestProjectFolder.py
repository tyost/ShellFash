'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model.ProjectFolder import ProjectFolder
try:
    # Python 3.3 and higher.
    from unittest import mock
except ImportError:
    # Python 3.2.
    import mock
from shellfash.model.ProjectNameValidator import ProjectNameValidator
from appdirs import AppDirs
import os


class TestProjectFolder(unittest.TestCase):
    '''
    Tests for ProjectFolder.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleNameValidator = mock.NonCallableMock(
            spec = ProjectNameValidator()
        )
        self.doubleAppDirs = mock.NonCallableMock(
            spec = AppDirs('shellfash')
        )
        self.doubleOpen = mock.Mock(spec = open)
    
        # Create instance of class under test.
        self.projectFolder = ProjectFolder(
            projectName = 'shellfash',
            _nameValidator = self.doubleNameValidator,
            _appDirs = self.doubleAppDirs,
            _open = self.doubleOpen
        )
    
    
    def test_constructor_projectname_good_verify_no_exception(self):
        self.doubleNameValidator.validate = mock.Mock(return_value=True)
        self.projectFolder = ProjectFolder(
            projectName = 'GoodName',
            _nameValidator = self.doubleNameValidator
        )

    def test_constructor_projectname_bad_verify_exception(self):
        self.doubleNameValidator.validate = mock.Mock(return_value=False)
        self.assertRaises(
            excClass = ValueError,
            callableObj = ProjectFolder,
            projectName = 'Bad/Name',
            _nameValidator = self.doubleNameValidator
        )
    
    
    def test__get_base_path__is_user_data_folder(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.assertEqual('base', self.projectFolder.get_base_path())
    
    
    def test__get_path__is_joined_user_data_folder(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.assertEqual(
            os.path.join('base', 'shellfash'),
            self.projectFolder.get_path()
        )
        
    
    def test__join__no_args(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.assertEqual(
            os.path.join('base', 'shellfash'),
            self.projectFolder.join()
        )
        
    def test__join__with_args(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.assertEqual(
            os.path.join('base', 'shellfash', 'one'),
            self.projectFolder.join('one')
        )
        self.assertEqual(
            os.path.join('base', 'shellfash', 'one', 'two', 'three'),
            self.projectFolder.join('one', 'two', 'three')
        )
    
    def test__join_open__return_value_is_from_open_builtin(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.doubleOpen.return_value = 'file object'
        returnValue = self.projectFolder.join_open(
            pathSequence = (),
        )
        self.assertEqual('file object', returnValue)
        
    def test__join_open__assert_extra_args_passed_to_open_builtin(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.projectFolder.join_open(
            (),
            1, 2, 3,
            newline='newline',
            closefd='closefd',
            opener='opener'
        )
        self.doubleOpen.assert_called_once_with(
            os.path.join('base', 'shellfash'),
            1, 2, 3,
            newline='newline',
            closefd='closefd',
            opener='opener'
        )
        
    def test__join_open__pathSequence_is_joined_user_data_folder(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.projectFolder.join_open(
            ('one', 'two')
        )
        self.doubleOpen.assert_called_once_with(
            os.path.join('base', 'shellfash', 'one', 'two')
        )
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
