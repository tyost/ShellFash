'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform
import unittest
from shellfash.test.helper.TestWindowCreator import TestWindowCreator
import time
try:
    # Python 3.3 and higher.
    from unittest import mock
except ImportError:
    # Python 3.2.
    import mock

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
        
        cls.WINDOW_TITLE = 'TestWin32API ShellFash Window '

    def setUp(self):
        self.windowCreator = TestWindowCreator()
        
        from shellfash.model.native.Win32API import Win32API
        self.win32API = Win32API()

    def tearDown(self):
        self.windowCreator.destroy_all()


    def test__EnumWindows__find_1_test_window__use_lparam(self):
        self.windowCreator.create(TestWin32API.WINDOW_TITLE, 1)
        windowHandle = self.windowCreator.get_handle(0)
        
        mockCallback = mock.Mock(return_value=True)
        self.win32API.EnumWindows(
            lpEnumFunc = mockCallback,
            lParam = 42
        )
        
        mockCallback.assert_any_call(windowHandle, 42)
        
    def test__EnumWindows__lpEnumFunc_returning_false_ends_early(self):
        self.windowCreator.create(TestWin32API.WINDOW_TITLE, 2)
        
        mockCallback = mock.Mock(return_value=False)
        self.win32API.EnumWindows(
            lpEnumFunc = mockCallback,
            lParam = 0
        )
        
        self.assertEqual(1, mockCallback.call_count)

    
    def test__IsWindowVisible__window_visible(self):
        self.windowCreator.create(TestWin32API.WINDOW_TITLE, 1)
        windowHandle = self.windowCreator.get_handle(0)
        self.assertTrue(self.win32API.IsWindowVisible(windowHandle))

    def test__IsWindowVisible__window_hidden(self):
        self.windowCreator.create(TestWin32API.WINDOW_TITLE, 1)
        testWindow = self.windowCreator.windows[0]
        testWindow.withdraw()
        
        windowHandle = self.windowCreator.get_handle(0)
        self.assertFalse(self.win32API.IsWindowVisible(windowHandle))


    def test__ShowWindow__minimize(self):
        self.windowCreator.create(TestWin32API.WINDOW_TITLE, 1)
        
        windowHandle = self.windowCreator.get_handle(0)
        self.win32API.ShowWindow(
            windowHandle,
            self.win32API.SW_MINIMIZE
        )    

        self.assertTrue(self.win32API.IsIconic(windowHandle))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
