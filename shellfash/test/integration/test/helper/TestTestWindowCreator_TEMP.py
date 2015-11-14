'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.test.helper.TestWindowCreator import TestWindowCreator
import platform
import time

@unittest.skipUnless(
    platform.system() in ('Windows', 'Linux'),
    'These tests only work on the Microsoft Windows or Linux X11 platforms.'
)
class TestTestWindowCreator_TEMP(unittest.TestCase):
    '''
    Tests for TestWindowCreator.
    '''

    def setUp(self):
        # Create class under test.
        self.windowCreator = TestWindowCreator()

    def tearDown(self):
        self.windowCreator.destroy_all()


    def test__create_and_destroy_all__one_window__verify_visibly_exists(self):
        self.windowCreator.create(
            titleBase = 'testCreateOneWindowVerifyVisiblyExists'
        )
        time.sleep(1)
        self.windowCreator.destroy_all()
        time.sleep(1)
        self.windowCreator.create(
            titleBase = 'testCreateOneWindowVerifyVisiblyExists'
        )
        time.sleep(1)
        
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