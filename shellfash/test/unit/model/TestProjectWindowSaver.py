'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from unittest import mock
from shellfash.model.ProjectWindowSaver import ProjectWindowSaver
from shellfash.model.ProjectName import ProjectName

class TestProjectWindowSaver(unittest.TestCase):
    '''
    Tests for ProjectWindowSaver.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleProjectName = mock.NonCallableMock(
            spec = ProjectName('myproject')
        )
        self.doubleProjectName.get_full_name = (
                mock.Mock(return_value='myproject'))
        self.doubleWindowFinder = mock.NonCallableMock()
        
        # Create instance of class under test.
        self.windowSaver = ProjectWindowSaver(
            _windowFinder = self.doubleWindowFinder
        )
    
    
    def test__save_visible__(self):
        self.fail('TODO')

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
