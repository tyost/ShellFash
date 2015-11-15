'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from appdirs import AppDirs
from fake_filesystem import FakeOsModule, FakeFilesystem
import os
from unittest import mock
import unittest

from shellfash.model.ProjectFolder import ProjectFolder
from shellfash.model.ProjectName import ProjectName


class TestProjectFolder(unittest.TestCase):
    '''
    Tests for ProjectFolder.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleProjectName = mock.NonCallableMock(
            spec=ProjectName('shellfash')
        )
        self.doubleProjectName.get_full_name = mock.Mock(
            return_value='shellfash'
        )
        self.doubleAppDirs = mock.NonCallableMock(
            spec=AppDirs('shellfash')
        )
        self.doubleOpen = mock.Mock(spec=open)
        self.fakeFilesystem = FakeFilesystem()
        self.fakeOs = FakeOsModule(self.fakeFilesystem)

        # Create instance of class under test.
        self.projectFolder = ProjectFolder(
            projectName=self.doubleProjectName,
            _appDirs=self.doubleAppDirs,
            _open=self.doubleOpen,
            _os=self.fakeOs
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
            pathSequence=(),
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

    def test__create__creates_new_folder(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.projectFolder.create()
        self.assertTrue(
            self.fakeOs.path.isdir(
                os.path.join('base', 'shellfash')
            )
        )

    def test__create__raises_exception_when_folder_exists(self):
        self.doubleAppDirs.user_data_dir = 'base'
        self.projectFolder.create()
        self.assertRaises(
            excClass=OSError,
            callableObj=self.projectFolder.create
        )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
