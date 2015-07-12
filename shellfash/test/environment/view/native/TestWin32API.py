'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform
import unittest
from shellfash.test.helper.TestWindowCreator import TestWindowCreator

@unittest.skipUnless(
    platform.system() == 'Windows',
    'These tests only work on the Microsoft Windows platform.'
)
class TestWin32API(unittest.TestCase):
    '''
    Tests for Win32API.
    '''

    @classmethod
    def setUpClass(cls):
        super(TestWin32API, cls).setUpClass()
        
        cls.windowCreator = TestWindowCreator()
        cls.WINDOW_TITLE = 'TestWin32API ShellFash Window '
        
    def setUp(self):
        from shellfash.view.native.Win32API import Win32API
        self.win32API = Win32API()

    def tearDown(self):
        self.windowCreator.destroy_all()

    def test_ShowWindow_minimize(self):
        TestWin32API.windowCreator.create(TestWin32API.WINDOW_TITLE, 1)
        
        windowHandle = TestWin32API.windowCreator.windows[0].GetHandle()
        self.win32API.ShowWindow(
            windowHandle,
            self.win32API.SW_MINIMIZE
        )    

        self.assertTrue(self.win32API.IsIconic(windowHandle))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
