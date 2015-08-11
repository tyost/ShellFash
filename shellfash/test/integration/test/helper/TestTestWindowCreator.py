'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.test.helper.TestWindowCreator import TestWindowCreator
from shellfash.model.WindowFinder import WindowFinder
import platform

@unittest.skipUnless(
    platform.system() == 'Windows',
    'These tests only work on the Microsoft Windows platform.'
)
class TestTestWindowCreator(unittest.TestCase):
    '''
    Tests for TestWindowCreator.
    '''

    def setUp(self):
        self.windowFinder = WindowFinder()
        
        # Create class under test.
        self.windowCreator = TestWindowCreator()

    def tearDown(self):
        self.windowCreator.destroy_all()


    def test__create__one_window__verify_visibly_exists(self):
        firstCount = len(self.windowFinder.get_visible_top_handles())
        self.windowCreator.create(
            titleBase = 'testCreateOneWindowVerifyVisiblyExists'
        )
        secondCount = len(self.windowFinder.get_visible_top_handles())
        self.assertEqual(firstCount + 1, secondCount)
         
    def test__create__multiple_windows__verify_visibly_exist(self):
        firstCount = len(self.windowFinder.get_visible_top_handles())
        self.windowCreator.create(
            titleBase = 'testCreateMultipleWindowsVerifyVisiblyExist',
            numWindows = 5
        )
        secondCount = len(self.windowFinder.get_visible_top_handles())
        self.assertEqual(firstCount + 5, secondCount)
         
    def test__create__two_back_to_back_calls__verify_exception(self):
        self.windowCreator.create(
            titleBase = 'testCreateTwoBackToBackCallsVerifyException'
        )
        self.assertRaises(
            excClass = RuntimeError,
            callableObj = self.windowCreator.create,
            titleBase = 'testCreateTwoBackToBackCallsVerifyException'
        )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()