'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model.WindowFinder import WindowFinder
import platform
from shellfash.test.helper.TestWindowCreator import TestWindowCreator

@unittest.skipUnless(
    platform.system() in ('Windows', 'Linux'),
    'These tests only work on the Microsoft Windows or Linux X11 platforms.'
)
class Test(unittest.TestCase):
    '''
    Tests for WindowFinder.
    '''

    def setUp(self):
        self.windowCreator = TestWindowCreator()
        self.windowFinder = WindowFinder()
    
    def tearDown(self):
        self.windowCreator.destroy_all()


    def test__constructor__no_arguments__verify_no_error(self):
        WindowFinder()
        
    def test__get_visible_top_handles__verify_handles_match(self):
        self.windowCreator.create(
            titleBase = 'testGetVisibleTopHandlesVerifyHandlesMatch',
            numWindows = 2
        )
        actualHandles = self.windowFinder.get_visible_top_handles()
        self.assertIn(self.windowCreator.get_handle(0), actualHandles)
        self.assertIn(self.windowCreator.get_handle(1), actualHandles)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()