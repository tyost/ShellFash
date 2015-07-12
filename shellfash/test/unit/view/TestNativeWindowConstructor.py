'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.view.NativeWindow import NativeWindow
from unittest.mock import Mock

class TestNativeWindowConstructor(unittest.TestCase):
    '''
    Tests for NativeWindow's constructor.
    '''

    def setUp(self):
        self.stubNativeWindow = Mock(
            is_supported = lambda: True
        )


    def tearDown(self):
        pass


    def test_WindowHandle_Missing(self):
        self.assertRaises(TypeError, NativeWindow)
        
    def test_WindowHandle_BadString(self):
        self.assertRaises(TypeError, NativeWindow,
                          '10b', self.stubNativeWindow)

    def test_WindowHandle_GoodString(self):
        nativeWindow = NativeWindow('42', self.stubNativeWindow)
        self.assertEqual(42, nativeWindow.get_handle())

    def test_WindowHandle_BadGetHandle(self):
        testObj = Mock(getHandle = "not function")
        self.assertRaises(TypeError, NativeWindow,
                          testObj, self.stubNativeWindow)

    def test_WindowHandle_GoodGetHandle(self):
        testObj = Mock(getHandle = lambda: 42)
        nativeWindow = NativeWindow(testObj, self.stubNativeWindow)
        self.assertEqual(42, nativeWindow.get_handle())
        
    def test__clsNativeWindow_If_Not_None_Then_Exception_Not_Swallowed(self):
        # The mock, pretending to be a constructor, doesn't return an object.
        testClsNativeWindow = Mock(return_value=None)
        self.assertRaises(AttributeError, NativeWindow,
                          42, testClsNativeWindow)
 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()