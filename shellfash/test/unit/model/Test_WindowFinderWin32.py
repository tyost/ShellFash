'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model._WindowFinderWin32 import _WindowFinderWin32
try:
    # Python 3.3 and higher.
    from unittest import mock
except ImportError:
    # Python 3.2.
    import mock

class Test_WindowFinderWin32(unittest.TestCase):
    '''
    Tests for _WindowFinderWin32.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.win32 = mock.NonCallableMock()
        self.win32.EnumWindows = mock.Mock()
    
        # Create instance of class under test.
        self.windowFinder = _WindowFinderWin32(
            _win32 = self.win32
        )

    
    def _fakeEnumWindows(self, windowHandleList):
        '''
        Sets up a fake for EnumWindows that calls the provided callback
        function with each window handle in windowHandleList.
        '''
        def EnumWindowsFake(lpEnumFunc, lParam):
            for handle in windowHandleList:
                if not lpEnumFunc(handle, lParam):
                    break
            return True
        self.win32.EnumWindows = EnumWindowsFake


    def test__get_visible_top_handles__no_windows(self):
        self._fakeEnumWindows([])

        returnValue = self.windowFinder.get_visible_top_handles()
        self.assertEqual([], returnValue)

    def test__get_visible_top_handles__multiple_windows__all_visible__all_top_level(self):
        self._fakeEnumWindows([42, 43])
        self.win32.IsWindowVisible = mock.Mock(return_value=True)
        
        returnValue = self.windowFinder.get_visible_top_handles()
        self.assertEqual([42, 43], returnValue)
        
    def test__get_visible_top_handles__multiple_windows__some_visible__all_top_level(self):
        VISIBLE_HANDLE = 42
        INVISIBLE_HANDLE = 43
        
        self._fakeEnumWindows([VISIBLE_HANDLE, INVISIBLE_HANDLE])
        
        def stubIsWindowVisible(hWnd):
            if hWnd == INVISIBLE_HANDLE:
                return False
            else:
                return True
        self.win32.IsWindowVisible = stubIsWindowVisible
                
        returnValue = self.windowFinder.get_visible_top_handles()
        self.assertEqual([VISIBLE_HANDLE], returnValue)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()