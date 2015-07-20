'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model.ProjectFolder import ProjectFolder
from shellfash.model.ProjectName import ProjectName

class TestProjectFolder(unittest.TestCase):
    '''
    Integration tests for ProjectFolder.
    '''

    def setUp(self):
        # Create instance of class under test.
        self.projectFolder = ProjectFolder(
            projectName = ProjectName('shellfash'),
        )


    def test__get_base_path__no_end_slash(self):
        path = self.projectFolder.get_base_path()
        self.assertTrue(path[-1] != '/')
        self.assertTrue(path[-1] != '\\')
        
    def test__get_project_path__no_end_slash(self):
        path = self.projectFolder.get_path()
        self.assertTrue(path[-1] != '/')
        self.assertTrue(path[-1] != '\\')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()